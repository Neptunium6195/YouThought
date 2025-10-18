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

def load_follow_ups():
    follow_ups = {}
    if os.path.exists('follow_ups.json'):
        with open('follow_ups.json', 'r') as f3:
            follow_ups = json.load(f3)
    else:
        print("follow_ups.json error")
    return follow_ups

chatHistory = load_chat_history()
responses = load_responses()
followUps = load_follow_ups()
problem = 8

@app.route('/', methods=['GET', 'POST'])

def index():
    global chatHistory, followUps, problem
    if request.method == 'POST':
        user_message = request.form.get('user-input', '').strip()
        chatHistory.append( ("user", user_message))
        if "distract" in user_message or "focus" in user_message:
            bot_response = random.choice(responses["distracted"])
            problem = 1
        elif "later" in user_message or "procrasinate" in user_message or "procrastinating" in user_message:
            bot_response = random.choice(responses["procrastinate"])
            problem = 0
        elif "lock in" in user_message or "locked in" in user_message or "focus on" in user_message:
            bot_response = random.choice(responses["lock in"])
            problem = 2
        elif "start" in user_message or "starting" in user_message or "begin" in user_message:
            bot_response = random.choice(responses["starting"])
            problem = 3
        elif "don't want to" in user_message or "do not want to" in user_message or "dont want to" in user_message:
            bot_response = random.choice(responses["don't want to"])
            problem = 4
        elif "phone" in user_message or "social media" in user_message or "instagram" in user_message or "tiktok" in user_message or "snapchat" in user_message:
            bot_response = random.choice(responses["phone"])
            problem = 6
        elif "tired" in user_message or "fatigue" in user_message or "exhausted" in user_message or "sleepy" in user_message:
            bot_response = random.choice(responses["tired"])
            problem = 5
        elif "motivate" in user_message or "motivation" in user_message or "motivated" in user_message or "inspire" in user_message or "inspiration" in user_message:
            bot_response = random.choice(responses["motivation"])
            problem = 7
        else:
            bot_response = random.choice(responses["default"])
            problem = 8
        chatHistory.append( ("Bobot", bot_response))
        with open('chat_history.txt', 'a') as f:
            f.write(f"user: {user_message}\n")
            f.write(f"Bobot: {bot_response}\n")
        return redirect(url_for('index', showFollowUps = 1))
    return render_template("index.html", chat_history=chatHistory, follow_ups=followUps, problem=problem)
if __name__ == '__main__':
    app.run(debug=True)