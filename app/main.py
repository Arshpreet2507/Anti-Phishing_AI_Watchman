# main.py

import os
import sys

# 🔥 THIS IS THE IMPORTANT FIX
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR)

print("🚀 main.py started", flush=True)
from attack_simulation import simulate_attack
from detector import rule_based_score
from ai_module import ai_predict
from response import take_action

print("🔐 Anti-Phishing AI Watchman 🔐", flush=True)

def run():
    text = input("Enter email/message text:\n")

    rule_score, reasons = rule_based_score(text)

    ai_result, ai_prob = ai_predict(text)
    ai_score = ai_prob * 100 if ai_result == 1 else 0

    # 🔥 IMPORTANT FIX: if AI model not trained, rely on rule-based score
    if ai_prob == 0.0:
     final_risk = rule_score
    else:
     final_risk = min(100, int((rule_score + ai_score) / 2))


    action, layer = take_action(final_risk, text)
    

    print("\n--- Analysis Result ---")
    print("Reasons:", reasons)
    print(f"AI Confidence: {round(ai_prob*100,2)}%")
    print(f"Final Risk Score: {final_risk}%")
    print("Action:", action)
    print("Security Layer:", layer)
    
    if final_risk >= 40:
     print("\n🚨 High-risk message detected!")
     print("▶ Simulating post-phishing attack...\n")
     simulate_attack()

if __name__ == "__main__":
    run()
