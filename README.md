# EchoMail
AI-powered communication assistant that fetches, analyzes, and organizes your emails intelligently. It classifies messages, extracts key insights, and generates smart responses for faster communication.

# Project Structure
'''
ai-comm-assistant/
│
├── backend/
│   ├── app.py                  # FastAPI backend server
│   ├── email_retrieval.py      # Email fetching & filtering logic
│   ├── nlp_utils.py            # Sentiment, priority, info extraction
│   ├── response_generator.py   # LLM-based auto-response logic
│   ├── crud.py                 # Database CRUD operations
│   ├── db.py                   # Database connection/setup
│   ├── models/
│   │   └── email.py            # SQLAlchemy Email model
│   └── requirements.txt        # Backend dependencies
│
├── frontend/
│   ├── src/
│   │   ├── components/         # React components (EmailList, Dashboard, etc.)
│   │   ├── pages/              # Main pages (Home, Analytics, etc.)
│   │   ├── App.js              # Main React app
│   │   └── index.js            # Entry point
│   ├── public/                 # Static assets
│   └── package.json            # Frontend dependencies
│
├── README.md                   # Project overview & setup instructions

'''
