
from flask import Flask, request, send_from_directory, redirect
import data_structs as ds


app = Flask(__name__)






@app.route('/')
def hello():
    return redirect("/static/chat_app_2/chat2.html", code=302)



@app.route('/photo', methods=['POST'])
def photo():
    file = request.files['file']

    file.save("static/web_files/"+ file.filename)

    return { "status": "ok", "url": "/static/web_files/"+ file.filename }


@app.route('/support/message', methods=['POST'])
def support_message():
    import telebot
    import config
    email = request.json['email']
    message = request.json['message']

    message_data = "email - "+email + "message: "+message

    bot = telebot.TeleBot(config.tg_token)
    bot.send_message(config.group_id, message_data)






@app.route('/chat', methods = ['POST'])
def chat_message():
    command = request.json['message']
    answer = {}

    if(command in ds.all_commands):
        answer = ds.command_answers[command]
    else:
        answer = { "answer": "unknown command", "commands":[]}

    return answer


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)



@app.route('/commands')
def all_commands():
    answer = {'data': list(ds.viewed_cmds)}
    return answer

