import requests

API_URL = "http://127.0.0.1:8000/predict"

def detect_phishing(email_text):
    response = requests.post(
        API_URL,
        json={"text": email_text}
    )

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "prediction": "Error",
            "risk_score": 0,
            "risk_level": "Backend not reachable"
        }