import webview
import threading
import requests
import winsound
import random
import sys
import os

# --- 1. Path Helper for EXE ---
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- 2. Motivation Quotes ---
QUOTES = [
    

    "You have the power to turn every \"no\" into a \"not yet.\"",
    "The only version of yourself you should compare yourself to is the one from yesterday.",
    "Your hard work today is the foundation for your success tomorrow.",
    "Believe in the process as much as you believe in the goal.",
    "Don’t just wait for the opportunity; create it.",
    "Small steps in the right direction lead to the biggest changes.",
    "Your resilience is your greatest asset—keep pushing forward.",
    "Every expert was once a beginner who didn’t give up.",
    "Focus on the progress, not just the perfection.",
    "You are capable of achieving everything you’ve set your mind to.",
    "The world needs the unique perspective that only you can bring.",
    "Let your ambition be louder than your fears.",
    "Success isn’t just about what you accomplish; it’s about who you become.",
    "Stay consistent, stay curious, and stay focused.",
    "Remember that growth often happens outside of your comfort zone.",
    "You don’t have to see the whole staircase to take the first step.",
    "Your dedication is what sets you apart from the crowd.",
    "Keep building, keep learning, and keep evolving.",
    "There is no limit to what you can achieve when you trust yourself.",
    "You’ve got this—one day at a time, one win at a time."
]


# --- 3. API Logic ---
class Api:
    def trigger_py_alarm(self):
        def _play():
            winsound.Beep(1000, 1000)
        threading.Thread(target=_play).start()

    def send_telegram_py(self, user_msg):
        def _send():
            # ==============================
            # PASTE YOUR KEYS HERE
            # ==============================
            token = "8529630607:AAFoYwbpzA4hmm0juTQUR0I0wy5w3L6w_4g"
            chat_id = "6154899005"
            # ==============================
            
            final_msg = user_msg
            if not final_msg or final_msg.strip() == "":
                final_msg = f"Chinmaya,\n {random.choice(QUOTES)}"
            else:
                final_msg = f"CHINMAYA REMINDER : {final_msg}"

            try:
                url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={final_msg}"
                requests.get(url)
            except Exception as e:
                print(f"Error: {e}")

        t = threading.Thread(target=_send)
        t.start()

# --- 4. Main Execution ---
if __name__ == '__main__':
    api = Api()
    html_file = resource_path('index.html')

    window = webview.create_window(
        'Neon Chrono', 
        html_file, 
        width=420, 
        height=720, 
        resizable=False, 
        js_api=api
    )
    webview.start()