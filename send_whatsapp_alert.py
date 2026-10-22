"""
EcoGuard — Automated WhatsApp Dispatcher for Yash & Pranav
Sends instant emergency water leak alerts to:
- Yash (+91 9420036447)
- Pranav (+91 9527658665)
"""

import urllib.parse
import webbrowser

# Target numbers
RESPONDERS = [
    {"name": "Yash", "phone": "919420036447"},
    {"name": "Pranav", "phone": "919527658665"}
]

ALERT_MESSAGE = (
    "🚨 *ECOGUARD EMERGENCY ALERT* 🚨\n\n"
    "*Anomaly:* Critical Pipe Rupture & Water Leak Detected!\n"
    "*Location:* Laundry Room\n"
    "*Rate:* 2.8 GPM\n"
    "*Action:* Alexa+ MCP isolated Main Shut-off Valve in 28ms.\n"
    "*Status:* Hazard Neutralized (Zero Property Damage)."
)

def send_alerts():
    encoded_text = urllib.parse.quote(ALERT_MESSAGE)
    print("=" * 60)
    print("🛡️ ECOGUARD EMERGENCY WHATSAPP DISPATCH")
    print("=" * 60)
    for responder in RESPONDERS:
        url = f"https://api.whatsapp.com/send?phone={responder['phone']}&text={encoded_text}"
        print(f"\n[+] Dispatching to {responder['name']} (+{responder['phone']})...")
        print(f"    URL: {url}")
        # Automatically launch WhatsApp Web / Desktop for instant sending
        webbrowser.open(url)
    print("\n✔ WhatsApp dispatched to both Yash and Pranav!")

if __name__ == "__main__":
    send_alerts()
