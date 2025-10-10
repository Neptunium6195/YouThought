from flask import Flask, render_template, request, redirect, url_for
import random, os
app = Flask(__name__)
with open('chat_history.txt', 'r') as f:
    lines = f.readlines()

responses = {
    "procrastinate": [
        "Why do today what you can put off until tomorrow?",
        "Procrastination is the art of keeping up with yesterday."
    ],
    "distracted": [
        "Focus is the key to success.",
        "Stay on track and avoid distractions.",
        "Put your phone or any other distractions in another room."
    ],
    "default": [
        "I believe in you! What's your main task right now?"
    ]
}
chatHistory = []

def load_chat_history():
    if os.path.exists('chat_history.txt'):
        with open('chat_history.txt', 'r') as f:
            for line in f:
                if line.startswith("user:"):
                    chatHistory.append(("user", line[5:].strip()))
                elif line.startswith("Bobot:"):
                    chatHistory.append(("Bobot", line[6:].strip()))
    return chatHistory
load_chat_history()
@app.route('/', methods=['GET', 'POST'])

def index():
    global chatHistory
    if request.method == 'POST':
        user_message = request.form.get('user-input', '').strip()
        chatHistory.append(("user", user_message))
        if "distract" in user_message or "focus" in user_message:
            bot_response = random.choice(responses["distracted"])
        elif "later" in user_message or "procrasinate" in user_message or "procrastinating" in user_message:
            bot_response = random.choice(responses["procrastinate"])
        else:
            bot_response = random.choice(responses["default"])
        chatHistory.append(("Bobot", bot_response))
        with open('chat_history.txt', 'a') as f:
            f.write(f"user: {user_message}\n")
            f.write(f"Bobot: {bot_response}\n")
        return redirect(url_for('index'))
    return render_template("index.html", chat_history=chatHistory)
if __name__ == '__main__':
    app.run(debug=True)