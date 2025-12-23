from detector import detect_phishing

def start_ui():
    print("=" * 50)
    print("🛡️  Anti-Phishing Detection System")
    print("Powered by FastAPI + ML Model")
    print("=" * 50)

    while True:
        print("\nEnter email content (or type 'exit' to quit):\n")
        email_text = input(">> ")

        if email_text.lower() == "exit":
            print("\nExiting Anti-Phishing System. Stay safe! 👋")
            break

        if email_text.strip() == "":
            print("⚠️ Email content cannot be empty.")
            continue

        print("\n🔍 Analyzing email...\n")

        # Call FastAPI via detector
        result = detect_phishing(email_text)

        # Display result
        print("📌 Prediction :", result.get("prediction"))
        print("📊 Risk Score :", f"{result.get('risk_score')}%")
        print("🚦 Risk Level :", result.get("risk_level"))
        print("-" * 50)