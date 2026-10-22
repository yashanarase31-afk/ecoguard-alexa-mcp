"""
EcoGuard — Real SMS Text Message Dispatcher
Sends instant SMS Text Messages to:
- Yash (+91 9420036447)
- Pranav (+91 9527658665)
"""

import sys
import json
import urllib.parse
import webbrowser
try:
    import urllib.request as urllib_req
except ImportError:
    import urllib2 as urllib_req

RESPONDERS = [
    {"name": "Yash", "phone": "+919420036447"},
    {"name": "Pranav", "phone": "+919527658665"}
]

SMS_MESSAGE = (
    "🚨 ECOGUARD ALERT: Critical Water Leak detected in Laundry Room (2.8 GPM). "
    "Alexa+ MCP isolated main valve automatically. Status: Safe."
)

def send_via_textbelt(phone_number, message):
    """Sends free SMS via TextBelt Gateway"""
    url = "https://textbelt.com/text"
    data = urllib.parse.urlencode({
        "phone": phone_number,
        "message": message,
        "key": "textbelt"  # Free tier key (1 free SMS per day)
    }).encode("utf-8")
    
    req = urllib_req.Request(url, data=data, headers={"User-Agent": "EcoGuard-SMS/1.0"})
    try:
        with urllib_req.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result
    except Exception as e:
        return {"success": False, "error": str(e)}

def dispatch_sms():
    print("=" * 65)
    print("🛡️ ECOGUARD REAL SMS TEXT MESSAGE DISPATCHER")
    print("=" * 65)
    
    for responder in RESPONDERS:
        name = responder["name"]
        phone = responder["phone"]
        print(f"\n[+] Sending Real SMS Text to {name} ({phone})...")
        
        # 1. Try sending via Textbelt Free Gateway
        res = send_via_textbelt(phone, SMS_MESSAGE)
        if res.get("success"):
            print(f"    ✔ SMS Sent successfully via Gateway! (ID: {res.get('textId')})")
        else:
            print(f"    ⚠️ Gateway response: {res.get('error', 'Quota limit reached or carrier filter')}")
            print(f"    [Fallback] Launching Native SMS handler for {name}...")
            # 2. Fallback to native SMS protocol
            sms_url = f"sms:{phone}?body={urllib.parse.quote(SMS_MESSAGE)}"
            webbrowser.open(sms_url)

    print("\n" + "=" * 65)
    print("✔ SMS Dispatch cycle complete!")
    print("=" * 65)

if __name__ == "__main__":
    dispatch_sms()
