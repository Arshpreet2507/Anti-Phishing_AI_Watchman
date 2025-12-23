# ai_model.py
# Handles ML-based phishing prediction

import joblib
import os

MODEL_PATH = "../model/phishing_model.pkl"
VECTORIZER_PATH = "../model/vectorizer.pkl"

# Check if model files exist
if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    print("⚠️ AI model not found. Please train the model first.")
    model = None
    vectorizer = None
else:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

def ai_predict(text):
    """
    Returns:
    prediction (0 = legit, 1 = phishing)
    probability (confidence score)
    """
    if model is None or vectorizer is None:
        # Fallback if AI model is missing
        return 0, 0.0

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    probability = max(model.predict_proba(X)[0])

    return prediction, probability
