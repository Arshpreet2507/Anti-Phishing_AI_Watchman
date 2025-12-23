import time
import logging
import os

# 🔥 Correct log path (absolute, safe)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "..", "logs", "alerts.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def simulate_attack():
    print("\n📩 Phishing attachment opened...")
    time.sleep(1)

    print("⚠️ Executing hidden malicious script...")
    time.sleep(1)

    print("🌐 Attempting outbound connection to attacker server...")
    time.sleep(1)

    attacker_server = "unknown-server[.]com"
    print(f"❌ Suspicious connection attempt blocked: {attacker_server}")

    logging.warning(
        f"SIMULATED ATTACK BLOCKED | Destination: {attacker_server}"
    )

    print("🛡️ Watchmen Action: CONNECTION BLOCKED")
    print("🔒 System Status: SAFE\n")
