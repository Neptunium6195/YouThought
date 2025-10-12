from flask import Flask, render_template, request, redirect, url_for
import random, os, json
app = Flask(__name__)
chatHistory = []

def load_chat_history():
    if os.path.exists('chat_history.txt'):
        with open('chat_history.txt', 'r') as f:
            for line in f:
                if line.startswith("user:"):
                    chatHistory.insert(0, ("user", line[5:].strip()))
                elif line.startswith("Bobot:"):
                    chatHistory.insert(0, ("Bobot", line[6:].strip()))
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
        chatHistory.insert(0, ("user", user_message))
        if "distract" in user_message or "focus" in user_message:
            bot_response = random.choice(responses["distracted"])
        elif "later" in user_message or "procrasinate" in user_message or "procrastinating" in user_message:
            bot_response = random.choice(responses["procrastinate"])
        else:
            bot_response = random.choice(responses["default"])
        chatHistory.insert(0, ("Bobot", bot_response))
        with open('chat_history.txt', 'a') as f:
            f.write(f"user: {user_message}\n")
            f.write(f"Bobot: {bot_response}\n")
        return redirect(url_for('index'))
    return render_template("index.html", chat_history=chatHistory)
if __name__ == '__main__':
    app.run(debug=True)