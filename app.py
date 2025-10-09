from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)
def home():
    return "welcome, unfortunately"
if __name__ == '__main__':
    app.run(debug=True)

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
@app.route('/', methods=['GET', 'POST'])

def index():
    global chatHistory
    if request.method == 'POST':
        #user_message = request.form["message"].lower()
        user_message = request.form.get('user_input')
        chatHistory.append(("user", user_message))
    if "later" in user_message or "procrasinate" in user_message:
        bot_response = random.choice(responses["procrastinate"])
    else:
        bot_message = random.choice(responses["default"])
    chatHistory.append(("bot", bot_response))
    return redirect(url_for('index'))
    return render_template("index.html", chat_history=chat_history)