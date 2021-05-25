from flask import Flask, request, send_from_directory, redirect
import data_structs as ds

app = Flask(__name__)


@app.route('/')
def hello():
    return redirect("/static/chat_app_2/chat2.html", code=302)


def send_img_to_tg(name, email):
    import telebot
    import config

    bot = telebot.TeleBot(config.tg_token)

    with open("static/web_files/" + name, 'rb') as f:
        bot.send_photo(chat_id=config.group_id, photo=f, caption=email)


@app.route('/photo', methods=['POST'])
def photo():
    file = request.files['file']
    email = request.form['user']

    file.save("static/web_files/" + file.filename)

    send_img_to_tg(file.filename, email)

    return {"status": "ok", "url": "/static/web_files/" + file.filename}


@app.route('/support/message', methods=['POST'])
def support_message():
    import telebot
    import config
    email = request.json['email']
    message = request.json['message']

    message_data = "email: " + email + "\nmessage: " + message + "\nWeb_client"

    print(message_data)

    bot = telebot.TeleBot(config.tg_token)
    bot.send_message(config.group_id, message_data)

    return {'status': 'ok'}


@app.route('/chat', methods=['POST','GET'])
def chat_message():

    meth = request.method

    command = request.json['message']
    answer = {}

    if (command in ds.all_commands):
        answer = ds.command_answers[command]
    else:
        answer = {"answer": "unknown command", "commands": []}

    return answer


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


@app.route('/commands')
def all_commands():
    answer = {'data': list(ds.viewed_cmds)}
    return answer
