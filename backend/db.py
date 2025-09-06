from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define Base here
Base = declarative_base()

# Update with your PostgreSQL credentials
DATABASE_URL = "postgresql+psycopg2://ai_comm_user:password@localhost:5432/ai_comm_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    from models.email import Email  # import here to register models
    Base.metadata.create_all(bind=engine)
