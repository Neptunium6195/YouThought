from flask import Flask
import random
app = Flask(__name__)
@app.route('/')
def home():
    return "welcome, unfortunately"
if __name__ == '__main__':
    app.run(debug=True)

responses = {
    "procrastinate", "procrasinate", "procrasinating", "procrasination" [
    "Why do today what you can put off until tomorrow?",
    "Procrastination is the art of keeping up with yesterday.",
    ],
    "distracted" [
    "Focus is the key to success.",
    "Stay on track and avoid distractions.",
    "Put your phone or any other distractions in another room.",
    ],
    "default" [
        "I believe in you! What's your main task right now?"
    ]
}
chatHistory = []

def home():
    global chatHistory
    if request.method == 'POST':
    user_message = request.form["message"].lower()