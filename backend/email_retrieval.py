import imaplib
import email
from email.header import decode_header
from nlp_utils import (
    analyze_sentiment,
    detect_priority,
    extract_contact_details,
    extract_customer_requirements,
    extract_sentiment_indicators
)

# Config
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "mmfazilkhan786@gmail.com"
PASSWORD = "ohai swqr htum ootl"
KEYWORDS = ["Support", "Query", "Request", "Help"]

def connect_imap():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.select("inbox")
    return mail

def fetch_emails(mail):
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()
    filtered_emails = []

    for eid in email_ids[-10:]:  # fetch last 10 emails
        status, msg_data = mail.fetch(eid, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        # Decode subject
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8")

        # Filter by keywords
        if not any(k.lower() in subject.lower() for k in KEYWORDS):
            continue

        from_ = msg.get("From")
        date_ = msg.get("Date")
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
        else:
            body = msg.get_payload(decode=True).decode()

        # NLP enrichment
        sentiment = analyze_sentiment(body)
        priority = detect_priority(body)
        contacts = extract_contact_details(body)
        requirements = extract_customer_requirements(body)
        indicators = extract_sentiment_indicators(body)

        # Metadata for analytics
        metadata = {
            "word_count": len(body.split()),
            "num_contacts": len(contacts.get("phone", [])) + len(contacts.get("alternate_email", [])),
            "num_requirements": len(requirements),
            "positive_count": len(indicators.get("positive_words", [])),
            "negative_count": len(indicators.get("negative_words", []))
        }

        filtered_emails.append({
            "id": int(eid),
            "sender_email": from_,
            "subject": subject,
            "body_text": body,
            "received_at": date_,
            "sentiment": sentiment,
            "priority": priority,
            "contact_phone": contacts.get("phone"),
            "alternate_email": contacts.get("alternate_email"),
            "requirements": requirements,
            "positive_words": indicators.get("positive_words"),
            "negative_words": indicators.get("negative_words"),
            "metadata": metadata
        })

    return filtered_emails

if __name__ == "__main__":
    mail = connect_imap()
    emails = fetch_emails(mail)
    for e in emails:
        print(f"Sender: {e['sender_email']}\nSubject: {e['subject']}\nDate: {e['received_at']}\n"
              f"Sentiment: {e['sentiment']} | Priority: {e['priority']}\n"
              f"Requirements: {e['requirements']}\n"
              f"Positives: {e['positive_words']} | Negatives: {e['negative_words']}\n"
              f"Metadata: {e['metadata']}\n{'-'*40}")
