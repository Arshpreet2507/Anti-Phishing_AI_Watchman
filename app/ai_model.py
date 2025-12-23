import os
import pickle

MODEL_PATH = "model/phishing_model.pkl"

def ai_predict(text):
    """
    Returns:
    (prediction, probability)
    prediction: 1 = phishing, 0 = safe
    probability: confidence score (0–1)
    """

    # 🔴 If model not trained yet (hackathon safe)
    if not os.path.exists(MODEL_PATH):
        print("⚠️ AI model not found. Please train the model first.")
        return 0, 0.0   # SAFE fallback

    try:
        with open(MODEL_PATH, "rb") as f:
            model, vectorizer = pickle.load(f)

        X = vectorizer.transform([text])
        prob = model.predict_proba(X)[0][1]
        pred = 1 if prob > 0.5 else 0

        return pred, prob

    except Exception as e:
        print("⚠️ AI error:", e)
        return 0, 0.0
