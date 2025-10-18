  
  <h1>🧠 AI-Powered Social Media Post Analyzer (Gemini)</h1>
  <p>A lightweight <strong>Flask web app</strong> using <strong>Google Gemini Generative AI</strong> to analyze social media posts and return structured JSON insights including sentiment, mood, and personality tone.</p>

  <hr>

  <section>
    <h2>🚀 Features</h2>
    <ul>
      <li>✨ <strong>Sentiment Analysis</strong> — Positive / Negative / Neutral</li>
      <li>😊 <strong>Mood Detection</strong> — e.g., Happy, Frustrated</li>
      <li>🧠 <strong>Personality Insights</strong> — detects tone or writer's attitude</li>
      <li>🌐 Simple Flask backend + REST API endpoint</li>
      <li>🔒 Local-only API key handling via <code>apikey.txt</code> or environment variable</li>
    </ul>
  </section>

  <section>
    <h2>⚙️ Setup &amp; Run</h2>
    <h3>1️⃣ Install dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>2️⃣ Add your Gemini API key</h3>
    <p>Create a file named <code>apikey.txt</code> in the project root and paste your Gemini API key inside.<br>
    Alternatively, set an environment variable:</p>
    <pre><code># macOS / Linux
export GEMINI_API_KEY='your_api_key_here'

# Windows
setx GEMINI_API_KEY "your_api_key_here"</code></pre>

    <h3>3️⃣ Run the app</h3>
    <pre><code>python app.py</code></pre>
    <p>Then open: <a href="http://127.0.0.1:5000" target="_blank">http://127.0.0.1:5000</a></p>
  </section>

  <section>
    <h2>📁 Project Structure</h2>
    <pre><code>AI-Powered Social Media Post Analyzer/
│
├── app.py                # Flask backend using google-generativeai
├── check_models.py       # Lists Gemini models
├── test_gemini.py        # Connectivity test
├── apikey.txt.template   # Example key file
├── requirements.txt      # Dependencies
├── sample_posts.txt      # Example posts
└── templates/ & static/  # Frontend files
</code></pre>
  </section>

  <section>
    <h2>🧩 Example Output</h2>
    <pre><code>{
  "sentiment": "Positive",
  "mood": "Excited",
  "personality_insight": "Optimistic, confident tone"
}</code></pre>
  </section>

  <section>
    <h2>🛠️ Technologies</h2>
    <ul>
      <li><strong>Backend:</strong> Flask, Flask-CORS</li>
      <li><strong>AI Model:</strong> Google Gemini (Generative AI API)</li>
      <li><strong>Language:</strong> Python 3.10+</li>
    </ul>
  </section>

  <section>
    <h2>⚠️ Security Notice</h2>
    <p>Never upload <code>apikey.txt</code> or share real API keys publicly. Revoke any accidentally exposed keys immediately in your Google AI console.</p>
  </section>

  <footer>
    <p>Created with ❤️ using Flask + Gemini AI.</p>
  </footer>
</body>
</html>
