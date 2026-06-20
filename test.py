import requests

response = requests.post(
    "http://127.0.0.1:5000/chat",
    json={
        "message": "What are Chandru's skills?"
    }
)

print(response.json())