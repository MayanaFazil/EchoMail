from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from db import Base

class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String(255))
    subject = Column(String(500))
    body = Column(Text)
    date = Column(DateTime)
    sentiment = Column(String(100))
    priority = Column(String(100))
    contact_phone = Column(Text)
    alternate_email = Column(Text)
    requirements = Column(Text)
    positive_words = Column(Text)
    negative_words = Column(Text)
    response = Column(Text)
    status = Column(String(50), default="pending")  # pending / resolved
