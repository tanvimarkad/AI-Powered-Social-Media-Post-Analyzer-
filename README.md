🧠 AI-Powered Social Media Post Analyzer (Gemini)

A simple Flask web app that uses Google’s Gemini Generative AI to analyze social media posts. It returns a structured JSON with insights like sentiment, mood, and personality tone.

🚀 Features

✨ Sentiment classification: Positive / Negative / Neutral

😊 Mood detection: short mood tag (e.g., Happy, Frustrated)

🧠 Personality insight: tone or intent of the writer

🌐 Simple Flask backend + easy-to-use REST API

🔒 Secure local API key handling (apikey.txt or environment variable)

⚙️ Setup & Run
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Add your Gemini API key

Create a file named apikey.txt in the project folder and paste your Gemini API key inside.
(Never share or commit this file.)

Alternatively, set the environment variable:

export GEMINI_API_KEY='your_api_key_here'  # macOS/Linux
setx GEMINI_API_KEY "your_api_key_here"    # Windows

3️⃣ Run the app
python app.py


Then open: http://127.0.0.1:5000/

📁 Project Structure
AI-Powered Social Media Post Analyzer/
│
├── app.py                # Flask app using google-generativeai
├── check_models.py       # Lists available Gemini models
├── test_gemini.py        # Simple Gemini API connectivity test
├── apikey.txt.template   # Template for local key storage
├── requirements.txt      # Dependencies
├── sample_posts.txt      # Example test posts
└── templates/ and static/ (frontend files)

🧩 Example Output
{
  "sentiment": "Positive",
  "mood": "Excited",
  "personality_insight": "Optimistic, confident tone"
}

🛠️ Technologies

Backend: Flask, Flask-CORS

AI Model: Google Gemini (Generative AI API)

Language: Python 3.10+

⚠️ Security Notice

Never upload your apikey.txt or include real API keys in commits or public repositories.
Revoke any accidentally exposed keys immediately from your Google AI console.
