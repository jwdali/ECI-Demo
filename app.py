from flask import Flask, render_template_string, jsonify, request
import os
import time
import random
from threading import Lock

# Lightweight sentiment analysis (no heavy ML model)
def analyze_sentiment(text):
    """Very simple rule-based sentiment (for demo only)."""
    text = text.lower()
    positive_words = ['good', 'great', 'excellent', 'love', 'happy', 'amazing', 'best']
    negative_words = ['bad', 'terrible', 'hate', 'awful', 'worst', 'disappointed', 'sad']
    
    pos_score = sum(1 for w in positive_words if w in text)
    neg_score = sum(1 for w in negative_words if w in text)
    
    if pos_score > neg_score:
        return "Positive", min(pos_score * 20, 100)
    elif neg_score > pos_score:
        return "Negative", min(neg_score * 20, 100)
    else:
        return "Neutral", 50

# Simulate CPU load during "inference"
def burn_cpu(seconds=0.8):
    end = time.time() + seconds
    while time.time() < end:
        _ = 3.141592653589793 ** 2

app = Flask(__name__)
counter = 0
lock = Lock()

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>🧠 Alibaba Cloud Sentiment Analyzer - Jawad Shah</title>
    <meta charset="utf-8">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; max-width: 800px; margin: 30px auto; padding: 0 20px; background: #f8f9fa; }
        .header { text-align: center; margin-bottom: 25px; }
        .pod-info { background: #e9ecef; padding: 12px; border-radius: 8px; margin: 20px 0; font-size: 14px; text-align: center; }
        textarea { width: 100%; height: 100px; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 6px; }
        .btn { background: #0070cc; color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-size: 16px; }
        .btn:hover { background: #005199; }
        .result { padding: 15px; margin: 20px 0; border-radius: 8px; text-align: center; font-size: 18px; font-weight: bold; }
        .positive { background: #d4edda; color: #155724; }
        .negative { background: #f8d7da; color: #721c24; }
        .neutral { background: #fff3cd; color: #856404; }
        .spinner { display: inline-block; width: 20px; height: 20px; border: 3px solid rgba(0,0,0,.2); border-top: 3px solid #0070cc; border-radius: 50%; animation: spin 1s linear infinite; margin-right: 10px; }
        @keyframes spin { to { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="header">
        <h1>🧠 Alibaba Cloud ACS Sentiment Analyzer</h1>
        <p>Powered by AI | Demo by Jawad Shah</p>
    </div>

    <div class="pod-info">
        <strong>Pod:</strong> {{ pod_name }} | 
        <strong>Analyzed:</strong> {{ counter }} texts
    </div>

    <textarea id="textInput" placeholder="Type a sentence to analyze sentiment... e.g., 'I love this service!'"></textarea><br>
    <button class="btn" onclick="analyze()">Analyze Sentiment</button>

    <div id="result" class="result" style="display:none;"></div>

    <script>
        function analyze() {
            const text = document.getElementById('textInput').value.trim();
            if (!text) return;

            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<span class="spinner"></span>Analyzing...';
            resultDiv.style.display = 'block';
            resultDiv.className = 'result';

            fetch('/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text: text})
            })
            .then(res => res.json())
            .then(data => {
                let cls = 'neutral';
                if (data.sentiment === 'Positive') cls = 'positive';
                else if (data.sentiment === 'Negative') cls = 'negative';
                resultDiv.className = 'result ' + cls;
                resultDiv.innerHTML = `${data.sentiment} (${data.confidence}%)`;
            })
            .catch(err => {
                resultDiv.className = 'result negative';
                resultDiv.innerHTML = 'Error: ' + err.message;
            });
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    global counter
    with lock:
        current_counter = counter
    return render_template_string(
        HTML_TEMPLATE,
        pod_name=os.getenv('HOSTNAME', 'unknown'),
        counter=current_counter
    )

@app.route('/analyze', methods=['POST'])
def analyze():
    global counter
    data = request.get_json()
    text = data.get('text', '')
    
    # Simulate AI inference load
    burn_cpu(0.8)
    
    sentiment, confidence = analyze_sentiment(text)
    
    with lock:
        counter += 1
    
    return jsonify({
        "sentiment": sentiment,
        "confidence": confidence
    })

@app.route('/healthz')
def healthz():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
