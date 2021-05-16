
from flask import Flask, request, send_from_directory, redirect
import data_structs as ds


app = Flask(__name__)



@app.route('/')
def hello():
    return redirect("/static/chat_app/chat5.html", code=302)



@app.route('/chat', methods = ['POST'])
def chat_message():
    command = request.json['command']
    answer = ''

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
    answer = { 'data': list(ds.all_commands) }
    return  answer

