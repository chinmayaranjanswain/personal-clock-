⏰ Neon Chrono
A futuristic, hybrid desktop clock application built with Python and HTML/CSS.

Neon Chrono is a lightweight desktop application that combines the powerful logic of Python with the beautiful styling capabilities of HTML5 & CSS3. It features a "Glassmorphism" UI, custom alarm sounds, and integrated Telegram Notifications to send alerts directly to your phone.

✨ Features
🎨 Premium UI: Modern "Glassmorphism" design with animated backgrounds and neon gradients using CSS3.

📱 Telegram Sync: Automatically sends alarm alerts to your phone via Telegram.

💬 Custom Messages: Type a reason (e.g., "Gym Time") to receive specific reminders, or get a Motivational Quote if you leave it blank.

🔊 Audio Alerts: Plays system sounds (Beep) or custom MP3s when the alarm rings.

🔌 Hybrid Engine: Uses pywebview to render HTML/CSS as a native desktop GUI.

📦 Portable: Can be compiled into a single .exe file using PyInstaller.

🛠️ Installation
1. Prerequisites
Ensure you have Python installed. Then, install the required libraries:

Bash
pip install pywebview requests pyinstaller
2. Project Structure
Your folder should look like this:

Plaintext
NeonChrono/
├── main.py          # The Python backend (Logic & Telegram)
├── index.html       # The UI (HTML/CSS/JS)
└── alarm.mp3        # (Optional) Custom alarm sound
⚙️ Configuration (Telegram)
To enable phone notifications, you must add your Telegram Bot credentials to main.py.

Open main.py.

Find the send_telegram_py function.

Replace the placeholders with your keys:

Python
# Inside main.py
token = "YOUR_BOT_TOKEN_HERE"  # Get from @BotFather
chat_id = "YOUR_CHAT_ID_HERE"  # Get from @userinfobot
🚀 How to Run
Method 1: Run as Python Script
Simply execute the main file:

Bash
python main.py
Method 2: Build as Standalone Application (.exe)
To create a portable .exe file that works on any Windows computer (even without Python installed):

Open your terminal in the project folder.

Run this specific command (it bundles the HTML file inside the EXE):

Bash
pyinstaller --noconsole --onefile --add-data "index.html;." main.py
Find your app in the dist folder.

🎮 How to Use
Launch the App.

Set a Message (Optional): Type a reminder like "Take Medicine" in the text box.

If you leave this empty, the app will send you a random motivational quote!

Set Time: Click the time picker and choose when the alarm should ring.

Activate: Click "ACTIVATE ALARM". The button will turn red and the inputs will lock.

Relax: When the time comes, your PC will beep, and your phone will buzz with the message!

🧩 Tech Stack
Backend: Python 3 (threading, requests, winsound)

Frontend: HTML5, CSS3 (Flexbox, CSS Variables, Keyframe Animations)

Bridge: Pywebview (Connects Python logic to JavaScript)

created with chinmaya 
