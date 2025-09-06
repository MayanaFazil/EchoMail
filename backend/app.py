from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from email_retrieval import connect_imap, fetch_emails
from db import SessionLocal, init_db
import crud
from response_generator import generate_response
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/emails/fetch")
def fetch_and_store_emails(db: Session = Depends(get_db)):
    """
    Fetch last 10 emails from IMAP, enrich with NLP, save to DB, and return them.
    Urgent emails are sorted first.
    """
    mail = connect_imap()
    emails = fetch_emails(mail)
    mail.logout()

    # Sort emails: Urgent first
    emails.sort(key=lambda x: 0 if x["priority"] == "Urgent" else 1)

    stored_emails = []
    for e in emails:
        # Prevent duplicates by checking subject+sender+date
        existing = db.query(crud.Email).filter(
            crud.Email.subject == e["subject"],
            crud.Email.sender == e["sender_email"],
            crud.Email.date == e["received_at"]
        ).first()

        if not existing:
            stored = crud.create_email(db, {
                "sender": e["sender_email"],
                "subject": e["subject"],
                "body": e["body_text"],
                "date": datetime.strptime(e["received_at"], '%a, %d %b %Y %H:%M:%S %z') if isinstance(e["received_at"], str) else e["received_at"],
                "sentiment": e["sentiment"],
                "priority": e["priority"],
                "contact_phone": str(e["contact_phone"]),
                "alternate_email": str(e["alternate_email"]),
                "requirements": str(e["requirements"]),
                "positive_words": str(e["positive_words"]),
                "negative_words": str(e["negative_words"]),
                "response": None,
                "status": "pending"
            })
            stored_emails.append(stored)
        else:
            stored_emails.append(existing)

    return {"emails": [e.__dict__ for e in stored_emails]}

@app.get("/emails/db")
def get_emails_from_db(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    emails = crud.get_emails(db, skip=skip, limit=limit)
    return {"emails": [e.__dict__ for e in emails]}

@app.post("/emails/respond/{email_id}")
def respond_to_email(email_id: int, db: Session = Depends(get_db)):
    """
    Generate AI response for an email and mark it as resolved.
    """
    email_record = crud.get_email_by_id(db, email_id)
    if not email_record:
        return {"error": "Email not found"}

    response = generate_response(
        email_record.body,
        email_record.sentiment,
        email_record.requirements
    )

    updated_email = crud.update_email_status(db, email_id, status="resolved", response=response)
    return {"email": updated_email.__dict__}
