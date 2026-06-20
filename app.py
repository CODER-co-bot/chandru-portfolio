from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

with open("portfolio_data.json", "r", encoding="utf-8") as f:
    portfolio_data = json.load(f)

@app.route("/")
def home():
    return "Portfolio Chatbot Backend Running!"

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    prompt = f"""
You are Chandru's Portfolio Assistant.

Use ONLY the following portfolio information:

{json.dumps(portfolio_data, indent=2)}

User Question:
{user_message}

Answer based only on the portfolio information.
If information is unavailable, say:
"I don't have information about that in Chandru's portfolio."
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    answer = response.json()["response"]

    return jsonify({"reply": answer})

if __name__ == "__main__":
    app.run(debug=True)