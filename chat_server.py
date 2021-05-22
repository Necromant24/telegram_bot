
from flask import Flask, request, send_from_directory, redirect
import data_structs as ds


app = Flask(__name__)



@app.route('/')
def hello():
    return redirect("/static/chat_app_2/chat2.html", code=302)

@app.route('/operators')
def operators():
    return { 'data': ds.operators }


#init new WS dialog
@app.route('/operator', methods = ['POST'])
def operator():

    operator = request.json['operator']
    user_email = request.json['email']

    ds.ws_operator_client[operator].append(user_email)
    ds.ws_dialog[(operator, user_email)] = []


    return { 'data': 'ваш оператор  - ' + operators }


@app.route('/ws/message', methods = ['POST'])
def ws_message():
    from_who = request.json['from']

    client_email = request.json['email']
    msg = request.json['message']
    client_operator = request.json['operator']


    ws = ds.ws_email_wsClient

    return {'status': 200}


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
    answer = { 'data': list(ds.viewed_cmds) }
    return  answer

