# AI-Powered Social Media Post Analyzer (Gemini)

## IMPORTANT - Security notice
You pasted an API key into the chat earlier. **Do not paste API keys in chat**. If you already pasted a key publicly, revoke it immediately from the provider's console.

This project DOES NOT include any API key. You must provide your Gemini key locally by either:
- creating `apikey.txt` in the project folder and pasting your key into it (local only), OR
- setting the `GEMINI_API_KEY` environment variable before running the app.

## Running locally (Windows PowerShell)
1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
2. Add your Gemini key to `apikey.txt` (create file) or set environment variable:
   ```powershell
   # One-time for this PowerShell session:
   $Env:GEMINI_API_KEY = 'YOUR_GEMINI_KEY_HERE'
   python app.py
   ```
3. Open http://127.0.0.1:5000 in your browser.

## Files
- `app.py` — Flask backend using google-generativeai (reads key from env or apikey.txt)
- `templates/index.html`, `static/css/style.css`, `static/js/main.js` — frontend
- `requirements.txt`
- `apikey.txt.template` — rename to `apikey.txt` and put your key inside (do NOT commit this file to git).
