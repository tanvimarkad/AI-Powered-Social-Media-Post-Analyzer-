from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import os, json, re

# -------------------------
# Initialize Flask
# -------------------------
app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# -------------------------
# Load Gemini API key
# -------------------------
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY and os.path.exists("apikey.txt"):
    with open("apikey.txt", "r", encoding="utf-8") as f:
        API_KEY = f.read().strip()

if not API_KEY:
    raise RuntimeError(
        "Please set GEMINI_API_KEY environment variable or place your key in apikey.txt"
    )

genai.configure(api_key=API_KEY)

# -------------------------
# Function to analyze post
# -------------------------
def analyze_with_gemini(post_text):
    try:
        prompt = f"""Analyze the following social media post and return a JSON object with keys:
1) sentiment -> one of "Positive", "Negative", "Neutral"
2) mood -> short mood label (e.g., Happy, Frustrated, Anxious)
3) personality_insight -> 1-2 short phrases describing the writer's tone

Post: "{post_text}"

Return ONLY a JSON object. Example:
{{"sentiment":"Negative","mood":"Frustrated","personality_insight":"Assertive, feels ignored"}}
"""

        # ✅ Use a valid Gemini 2.5 model
        model = genai.GenerativeModel("models/gemini-2.5-flash")

        response = model.generate_content(prompt)
        text = response.text.strip()

        # Extract JSON safely
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            return json.loads(m.group(0))
        else:
            return {"error": "No JSON found in response", "raw": text}

    except Exception as e:
        return {"error": str(e)}

# -------------------------
# Flask routes
# -------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        post_text = data.get('post', '').strip()
        if not post_text:
            return jsonify({"error": "No post text provided."}), 400
        result = analyze_with_gemini(post_text)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------------
# Run app
# -------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
