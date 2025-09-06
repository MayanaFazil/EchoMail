from sqlalchemy.orm import Session
from models.email import Email

def create_email(db: Session, email_data: dict):
    email = Email(**email_data)
    db.add(email)
    db.commit()
    db.refresh(email)
    return email

def get_emails(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Email).offset(skip).limit(limit).all()

def get_email_by_id(db: Session, email_id: int):
    return db.query(Email).filter(Email.id == email_id).first()

def update_email_status(db: Session, email_id: int, status: str, response: str = None):
    email = get_email_by_id(db, email_id)
    if email:
        email.status = status
        if response:
            email.response = response
        db.commit()
        db.refresh(email)
    return email
