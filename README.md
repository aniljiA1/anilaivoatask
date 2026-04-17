# 🚀 AI CRM for Healthcare Professionals (HCP)

An AI-powered CRM system designed for pharma sales reps to manage doctor interactions, analyze sentiment, and get intelligent follow-up suggestions.

---

## 📌 Features

* 🤖 **AI Chat Assistant** – Ask questions and get smart responses
* 📝 **Log Doctor Interactions** – Store notes with sentiment analysis
* 📊 **Sentiment Detection** – Automatically classify interactions
* 💡 **Next Action Suggestions** – AI recommends follow-ups
* ⚡ **FastAPI Backend + React Frontend**

---

## 🛠️ Tech Stack

### Frontend

* React.js (Vite)
* Redux Toolkit
* Axios
* Tailwind CSS

### Backend

* FastAPI
* Groq API (LLM)
* SQLAlchemy
* SQLite (can upgrade to PostgreSQL)

---

## 📂 Project Structure

```
ai-crm-hcp/
│
├── client/        # React frontend
│   ├── src/
│   └── .env
│
├── server/        # FastAPI backend
│   ├── main.py
│   ├── requirements.txt
│   ├── agent/
│   │   ├── tools.py
│   │   └── graph.py
│   └── db/
│       ├── database.py
│       └── models.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repo

```
git clone https://github.com/your-username/ai-crm-hcp.git
cd ai-crm-hcp
```

---

### 2️⃣ Backend Setup

```
cd server
pip install -r requirements.txt
```

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

Run backend:

```
uvicorn main:app --reload
```

---

### 3️⃣ Frontend Setup

```
cd client
npm install
```

Create `.env`:

```
VITE_API_URL=http://localhost:8000

http://127.0.0.1:8000/

http://127.0.0.1:8000/docs
```

Run frontend:

```
npm run dev

http://localhost:5173/

https://anilaivoatask.vercel.app/
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description            |
| ------ | -------- | ---------------------- |
| POST   | `/chat`  | AI chat response       |
| POST   | `/log`   | Log doctor interaction |

---

## 🚀 Deployment

### Backend (Render)

* Build: `pip install -r requirements.txt`
* Start: `uvicorn main:app --host 0.0.0.0 --port 10000`
  

### Deploy

 https://anilaivoatask.vercel.app/
---

## 🔥 Future Improvements

* 📈 Dashboard analytics
* 🧠 AI with doctor history context
* 🔔 Follow-up reminders
* 🗄️ PostgreSQL integration

---

## 👨‍💻 Author

**Anil Kumar**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
