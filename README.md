# 🛡️ EcoGuard — Autonomous Home Disaster & Safety Orchestrator

> **Built for the Amazon Developer Hackathon: Build, Ship, Shape**  
> *Category:* **Alexa+ (Model Context Protocol)**  
> *Stackable Challenges:* **AWS Builder** & **Open Source**  
> *Authors:* **Yash** & **Pranav**  
> *License:* MIT

[![MCP Protocol](https://img.shields.io/badge/Protocol-Model_Context_Protocol_v1.0-indigo)](https://modelcontextprotocol.io/)
[![Amazon Alexa+](https://img.shields.io/badge/Target-Alexa+_Agentic_Core-blue)](https://developer.amazon.com/)
[![AWS Bedrock](https://img.shields.io/badge/AI-Amazon_Bedrock_Claude_3.5-orange)](https://aws.amazon.com/bedrock/)
[![Zero-Click Auto-SMS](https://img.shields.io/badge/Dispatch-100%25_Autonomous_SMS-emerald)](https://aws.amazon.com/sns/)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)

---

## 💡 Overview

When home hazards strike—such as a catastrophic water pipe rupture, kitchen grease fire, or electrical surge—every second matters. Most smart homes only beep passively while damage multiplies.

**EcoGuard** transforms **Alexa+** into an ambient autonomous orchestrator using the **Model Context Protocol (MCP)**. By combining **Ring telemetry**, **Fire TV 10-foot UI**, **Bee wearable AI**, and **100% Autonomous Zero-Click SMS Dispatching to Yash & Pranav**, EcoGuard eliminates human delay and neutralizes hazards before they turn into catastrophes.

---

## 👥 Configured Emergency Responders (Zero-Click Auto-Dispatch)

| Name | Role | Mobile Number | Dispatch Mode |
| :--- | :--- | :--- | :--- |
| **Yash** | Primary Responder / Homeowner | `+91 9420036447` | **100% Automated** Background SMS & Network Push |
| **Pranav** | Co-Responder / Engineer | `+91 9527658665` | **100% Automated** Background SMS & Network Push |

---

## ⚡ The Cross-Device Flow

```mermaid
flowchart TD
    Sensor["1. Ring / Smart Sensor<br/>Detects burst pipe / thermal spike"] --> Alexa["2. Alexa+ Agentic Core (MCP Client)<br/>Evaluates threat with Bedrock LLM"]
    
    subgraph "EcoGuard MCP Server (FastMCP)"
        Alexa -- "JSON-RPC / SSE" --> Tools
        Tools --> ToolTV["broadcast_firetv_pip_alert()"]
        Tools --> ToolBee["send_bee_wearable_haptic_card()"]
        Tools --> ToolAutoSMS["auto_dispatch_sms(Yash, Pranav)"]
        Tools --> ToolValve["shut_off_utility_valve()"]
    end
    
    ToolTV --> FireTV["3. Fire TV Display<br/>Sliding Picture-in-Picture + D-pad prompt"]
    ToolBee --> Bee["4. Bee Wearable AI (Wrist)<br/>Haptic pulse + 1-tap cutoff card"]
    ToolAutoSMS --> PhoneYash["5. Yash (+91 9420036447)<br/>Auto-Dispatched Direct SMS (0 clicks)"]
    ToolAutoSMS --> PhonePranav["6. Pranav (+91 9527658665)<br/>Auto-Dispatched Direct SMS (0 clicks)"]
    ToolValve --> Actuator["7. Electromechanical Valve<br/>Utility cut in &lt;50ms (Zero damage)"]
```

1. **Detection:** A Ring Indoor Cam or water flow sensor flags a surge in water volume (2.8 GPM).
2. **Context & Reasoning:** The **Alexa+ Agentic Core** pulls live ambient telemetry (`home://telemetry/live`) via MCP resources. It deduces that someone is watching a movie in the living room while another user is outside in the garden.
3. **Living Room Alert (Fire TV):** Alexa+ calls `broadcast_firetv_pip_alert()`, interrupting the Fire TV stream with a smooth Picture-in-Picture live video feed and a 1-click D-pad action prompt.
4. **Wrist Alert (Bee Wearable):** Simultaneously, Alexa+ calls `send_bee_wearable_haptic_card()`, vibrating the wrist of the outdoor user with an interactive emergency card.
5. **Zero-Click Auto-SMS Dispatch:** Alexa+ executes `auto_dispatch_sms()`, transmitting SMS text messages directly to **Yash (+91 9420036447)** and **Pranav (+91 9527658665)** automatically without asking for confirmation.
6. **Neutralization:** The user confirms with a single click, and Alexa+ executes `shut_off_utility_valve()`, isolating the supply line in milliseconds.

---

## 🚀 Live Interactive Simulator

### How to Run:
1. Open https://yashanarase31-afk.github.io/ecoguard-alexa-mcp/ in any modern web browser.
2. Click **"Trigger Anomaly & Auto-SMS"** or **"🎬 Auto-Play Video Demo"**.
3. The system automatically fires the background SMS payload directly to **Yash** and **Pranav** instantly with **zero buttons to press**!
4. The screen shows the delivery receipts, latency in milliseconds, and real-time wire logs for your video recording.
5. Here is the demo video link and explanation of the project https://youtu.be/9dxwQv5vIOU?si=9ESIG0tXdPsPtGhh
