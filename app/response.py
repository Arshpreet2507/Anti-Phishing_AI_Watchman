import datetime

LOG_FILE = "logs/alerts.log"


def take_action(risk_score, text=""):
    """
    Decide action and security layer based on risk score
    """

    if risk_score >= 70:
        action = "🚨 PHISHING DETECTED - Block & Alert"
        layer = "Email Gateway / Network Firewall"
        log_alert(risk_score, text, action)

    elif risk_score >= 40:
        action = "⚠️ SUSPICIOUS - Warn User"
        layer = "User Level"
        log_alert(risk_score, text, action)

    else:
        action = "✅ SAFE"
        layer = "No Action Required"

    return action, layer


def log_alert(score, text, action):
    """
    Log alerts to file for demo purposes
    """
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(
                f"[{datetime.datetime.now()}] "
                f"Risk={score}% | Action={action} | Message={text[:80]}\n"
            )
    except Exception as e:
        print("Logging failed:", e)
