from flask import Flask, render_template, request, redirect, url_for
import random, os, json
app = Flask(__name__)
chatHistory = []

def load_chat_history():
    if os.path.exists('chat_history.txt'):
        with open('chat_history.txt', 'r') as f:
            for line in f:
                if line.startswith("user:"):
                    chatHistory.append( ("user", line[5:].strip()))
                elif line.startswith("Bobot:"):
                    chatHistory.append( ("Bobot", line[6:].strip()))
    else:
        print("chat_history.txt error")
    return chatHistory

def load_responses():
    responses = {}
    if os.path.exists('responses.json'):
        with open('responses.json', 'r') as f2:
            responses = json.load(f2)
    else:
        print("responses.json error")
    return responses

chatHistory = load_chat_history()
responses = load_responses()

@app.route('/', methods=['GET', 'POST'])

def index():
    global chatHistory
    if request.method == 'POST':
        user_message = request.form.get('user-input', '').strip()
        chatHistory.append( ("user", user_message))
        if "distract" in user_message or "focus" in user_message:
            bot_response = random.choice(responses["distracted"])
        elif "later" in user_message or "procrasinate" in user_message or "procrastinating" in user_message:
            bot_response = random.choice(responses["procrastinate"])
        elif "lock in" in user_message or "locked in" in user_message or "focus on" in user_message:
            bot_response = random.choice(responses["lock in"])
        elif "start" in user_message or "starting" in user_message or "begin" in user_message:
            bot_response = random.choice(responses["starting"])
        elif "don't want to" in user_message or "do not want to" in user_message or "dont want to" in user_message:
            bot_response = random.choice(responses["don't want to"])
        elif "phone" in user_message or "social media" in user_message or "instagram" in user_message or "tiktok" in user_message or "snapchat" in user_message:
            bot_response = random.choice(responses["phone"])
        elif "tired" in user_message or "fatigue" in user_message or "exhausted" in user_message or "sleepy" in user_message:
            bot_response = random.choice(responses["tired"])
        else:
            bot_response = random.choice(responses["default"])
        chatHistory.append( ("Bobot", bot_response))
        with open('chat_history.txt', 'a') as f:
            f.write(f"user: {user_message}\n")
            f.write(f"Bobot: {bot_response}\n")
        return redirect(url_for('index'))
    return render_template("index.html", chat_history=chatHistory)
if __name__ == '__main__':
    app.run(debug=True)