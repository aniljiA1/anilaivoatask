import os
from groq import Groq
from db.database import SessionLocal
from db.models import Interaction

# ✅ Models
MODEL_FAST = "llama-3.1-8b-instant"
MODEL_SMART = "llama-3.1-70b-versatile"

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ✅ 1. Log Interaction
def log_interaction(data):
    db = SessionLocal()
    try:
        prompt = f"""
        Classify sentiment as:
        positive / neutral / negative

        Text:
        {data['notes']}

        Return only one word.
        """

        response = client.chat.completions.create(
            model=MODEL_FAST,
            messages=[
                {"role": "system", "content": "You are a medical CRM assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        sentiment = response.choices[0].message.content.strip()

        interaction = Interaction(
            doctor=data["doctor"],
            notes=data["notes"],
            sentiment=sentiment
        )

        db.add(interaction)
        db.commit()
        db.refresh(interaction)

        return {
            "status": "logged",
            "id": interaction.id,
            "sentiment": sentiment
        }

    except Exception as e:
        db.rollback()
        return {"error": str(e)}

    finally:
        db.close()


# ✅ 2. Edit Interaction
def edit_interaction(data):
    db = SessionLocal()
    try:
        interaction = db.query(Interaction).filter(
            Interaction.id == data["id"]
        ).first()

        if not interaction:
            return {"error": "Not found"}

        interaction.notes = data.get("notes", interaction.notes)

        db.commit()

        return {"status": "updated"}

    except Exception as e:
        db.rollback()
        return {"error": str(e)}

    finally:
        db.close()


# ✅ 3. Get History
def get_hcp_history(data):
    db = SessionLocal()
    try:
        results = db.query(Interaction).filter(
            Interaction.doctor == data["doctor"]
        ).all()

        return [
            {
                "id": r.id,
                "notes": r.notes,
                "sentiment": r.sentiment
            }
            for r in results
        ]

    except Exception as e:
        return {"error": str(e)}

    finally:
        db.close()


# ✅ 4. Suggest Next Action
def suggest_next_action(data):
    try:
        prompt = f"""
        Based on this doctor interaction, suggest next best action:

        {data['notes']}

        Keep it short and practical.
        """

        response = client.chat.completions.create(
            model=MODEL_SMART,
            messages=[
                {"role": "system", "content": "You are a pharma sales assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )

        return {
            "suggestion": response.choices[0].message.content.strip()
        }

    except Exception as e:
        return {"error": str(e)}


# ✅ 5. Sentiment Analysis
def sentiment_analysis(data):
    try:
        prompt = f"""
        Classify sentiment as:
        positive / neutral / negative

        Text:
        {data['text']}

        Return only one word.
        """

        response = client.chat.completions.create(
            model=MODEL_FAST,
            messages=[
                {"role": "system", "content": "You are a sentiment analyzer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return {
            "sentiment": response.choices[0].message.content.strip()
        }

    except Exception as e:
        return {"error": str(e)}


# ✅ 6. AI CHAT (🔥 NEW - IMPORTANT)
def ai_chat(data):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are an AI CRM assistant for pharma sales reps.

                    - Help with doctor communication
                    - Suggest follow-ups
                    - Be professional and helpful
                    - Never say "I am not a doctor"
                    """
                },
                {"role": "user", "content": data["message"]}
            ],
            temperature=0.7
        )

        return {
            "reply": response.choices[0].message.content.strip()
        }

    except Exception as e:
        return {"error": str(e)}