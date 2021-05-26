import datetime
import sqlite3 as sql
import config

from flask import Flask, request, send_from_directory, redirect
import data_structs as ds
import messages

app = Flask(__name__)



def db_find_value(col_name, value):
    """ Check if value exists in database and return corresponding row, 'col_name' must be name of DB column
        DB columns in order: email, date, tariff, sub, tg_id, vk_id, fb_id, state, rate, review_time, received, verified """

    with sql.connect(config.db_file) as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM clients WHERE {col_name} = ?", (str(value).lower(),))
        res = cur.fetchall()

        if res:
            return res[0]

        return 0



# --------------------------------------------------
def client_info_msg(col_name, value):
    """ Make a message with client tariff info """

    info = db_find_value(col_name, value)
    if not info:
        return "No info about client"

    message = f"\U00002139\nemail: {info[0]}\n" \
              f"date: {info[1]}\n" \
              f"tariff: {info[2]}\n" \
              f"sub: {info[3]}\n"

    return message







@app.route('/')
def hello():
    return redirect("/static/chat_app_2/chat2.html", code=302)


def send_img_to_tg(name, email):
    import telebot
    import config

    bot = telebot.TeleBot(config.tg_token)

    message = client_info_msg("email",email) + "\nWeb_client"

    with open("static/web_files/" + name, 'rb') as f:
        bot.send_photo(chat_id=config.group_id, photo=f, caption=message)



@app.route("/email", methods=['POST'])
def email():
    client_email = request.json['email']

    if client_info_msg('email', client_email) == 'No info about client':
        with sql.connect(config.db_file) as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO clients (email) VALUES (?)", (client_email,))

            return {"status": "created new row"}

    return {"status": "already exists"}


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



def serve(app, host, port):
    app.run(host=host,port=port)
