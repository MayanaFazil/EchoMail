# EchoMail - AI-Powered Communication Assistant
AI-powered communication assistant that fetches, analyzes, and organizes your emails intelligently. It classifies messages, extracts key insights, and generates smart responses for faster communication.

**InboxIQ** is an AI-powered communication assistant that intelligently manages support emails.  
It fetches, filters, prioritizes, and extracts key information from emails, while generating context-aware draft responses, all displayed on a user-friendly dashboard.

## 🔎 Project Summary
Modern organizations receive hundreds or thousands of emails daily, many of which are support-related (queries, requests, help tickets).  
InboxIQ automates the support pipeline by:
- Fetching emails from IMAP/Gmail
- Filtering support-related messages
- Extracting contact and request details
- Classifying emails by sentiment and priority
- Generating AI-powered draft responses
- Displaying processed emails and analytics on a React dashboard

## 📁 Repository Layout
```
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

```

## ⚙️ Prerequisites
- Python 3.9+
- Node.js and npm
- Gmail or any IMAP-supported email account (enable App Password if using Gmail)
- (Optional) OpenAI API key or Hugging Face model API key for LLM responses

## Configure credentials

Database: Update backend/db.py if using PostgreSQL/MongoDB. SQLite works by default.

Email: Edit backend/email_retrieval.py:

```
EMAIL_ACCOUNT = "your_email@example.com"
EMAIL_PASS = "your_app_password"
IMAP_SERVER = "imap.gmail.com"
```

⚠️ Do not commit real credentials. For production, use a .env file.

LLM API (Optional): Add your OpenAI/Hugging Face key in backend/response_generator.py or via environment variable.

## Run Backend
```
cd backend

# Create virtual environment
python -m venv venv

# Activate venv
# macOS / Linux
source venv/bin/activate
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn app:app --reload --port 8000
```
Open API docs: http://127.0.0.1:8000/docs

## Run Frontend

Open a new terminal:
```
cd frontend
npm install
npm start
```
Open dashboard: http://localhost:3000/
```
| Route         | Description                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| `/dashboard`  | Main analytics dashboard; shows email stats, sentiment breakdown, priority, pending vs resolved emails. |
| `/emails`     | Lists all filtered emails with extracted details (sender, subject, date, priority, sentiment).          |
| `/emails/:id` | Detailed view of a single email, extracted metadata, and AI-generated draft reply (editable).           |
| `/navbar`     | Navigation bar to switch between pages (Dashboard, Emails, Analytics).                                  |
| `/home`       | Optional home/welcome page showing overview.                                                            |
```

## 🧠 Features
Email Retrieval & Filtering: Fetch emails via IMAP; filter by subject keywords: Support, Query, Request, Help.
Sentiment & Priority Analysis: Classify emails (Positive/Neutral/Negative) and mark urgent requests.
Contact Info Extraction: Detect phone numbers and alternate emails.
Context-Aware Draft Responses: Generate editable replies using RAG + LLM.
Dashboard Analytics: Track total emails, sentiment distribution, priority, pending vs resolved emails.

## 📄 Architecture & Approach
Emails are fetched via IMAP and filtered for support keywords. NLP modules extract metadata, compute sentiment, and determine priority. Emails are stored in a database and processed via a priority queue (urgent-first). A knowledge base provides context for the LLM to generate professional, empathetic draft responses. The React dashboard displays all emails, metadata, AI-generated drafts, and analytics in a structured, user-friendly manner.

