document.getElementById('analyzeBtn').addEventListener('click', async () => {
  const post = document.getElementById('postText').value.trim();
  if (!post) {
    alert('Please enter a post text to analyze.');
    return;
  }
  const btn = document.getElementById('analyzeBtn');
  btn.disabled = true;
  btn.textContent = 'Analyzing...';
  try {
    const res = await fetch('/analyze', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({post})
    });

    const data = await res.json();  // Will now always be JSON
    document.getElementById('resultArea').style.display = 'block';
    document.getElementById('resultBox').textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    document.getElementById('resultArea').style.display = 'block';
    document.getElementById('resultBox').textContent = 'Error: ' + e.message;
  } finally {
    btn.disabled = false;
    btn.textContent = 'Analyze';
  }
});

document.getElementById('exampleBtn').addEventListener('click', () => {
  const examples = [
    "I finally achieved my fitness goals this year! Feeling proud and strong.",
    "Nothing seems to work in my favor these days. Tired and hopeless.",
    "Excited to start my new job tomorrow! Can't wait to meet the team."
  ];
  document.getElementById('postText').value = examples.join('\n\n');
});
