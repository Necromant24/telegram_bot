import  messages
commands = '''
Оплата, В рублях ₽ или в гривнах ₴, В юанях ¥, Связаться с поддержкой,
Пробный период, 
Узнать больше, Блог,
Для Туркменистана, 
Сотрудничество, 
ZGC SHOP, 
Связаться с поддержкой

'''

# варианты ответа через 2 запятые
command_answers = \
    {
        "/Оплата": { "answer": messages.pay_type, "commands": [("В рублях ₽ или в гривнах ₴",'/rub'), ("В юанях ¥", "/yuan"), ("Связаться с поддержкой",'/sup')]},
        "/Пробный период": { "answer": messages.trial_text, "commands":[("Оплата",'/pay'), ("Связаться с поддержкой",'/sup')]},
        "/Узнать больше": { "answer": "Узнайте как заблокировать рекламу, какие появились сервера и многое другое", "commands": [["Блог",'/url']]},
        "/Для Туркменистана":  { "answer": messages.turk, "commands":[("Сайт обслуживания",'https://tm.zgc.su/'), ("Как подключить?",'https://sites.google.com/view/zgcvpn/try?authuser=0')]},
        "/Сотрудничество": { "answer": messages.coop, "commands":[["Сделать предложение",'/url']]},
        "/ZGC SHOP": { "answer": messages.shop, "commands":[("ZGC SHOP",'/url'), ("Связаться с поддержкой", '/market') ]},
        "/Связаться с поддержкой": { "answer": messages.coop, "commands":[("Первичная настройка", "/install"),("Другое", "/other"), ('ZGC SHOP','/market')]},



        "/urgent": {"answer": messages.first_install, "commands":[]},
        "/install": {"answer": messages.first_install, "commands":[]},
        "/other": {"answer": messages.support, "commands":[]},
        "/market": {"answer": 'Здравствуйте! Укажите, пожалуйста, продукт и вопросы по нему', "commands":[]},
        "/rub": {"answer": messages.first_install, "commands":[]},
        "/yuan": {"answer": messages.first_install, "commands":[]},
        "/sup": {"answer": messages.first_install, "commands":[]},
        "/pay": {"answer": messages.first_install, "commands":[]},
        "/url": {"answer": messages.first_install, "commands":[]},

    }


viewed_cmds = [ "/Оплата", "/Пробный период", "/Узнать больше",  "/Для Туркменистана", "/Сотрудничество", "/ZGC SHOP", "/Связаться с поддержкой" ]


operators = ['operator1', 'operator2']

# support operator with client pairs
ws_operator_client = { 'op1': [] }


# client email - key ; websocket object - value
client_ws = {}


# operator name - key ; websocket object - value
operator_ws = {}


ws_conn = 'object of websocket connection'

ws_email_wsClient = {'client_email': ws_conn}


def send_ws_msg(who, client_email, operator, message):

    if who == 'operator':

        client_ws[client_email].send(message)

    elif who == 'client':
        operator_ws[operator].send(message)




# waterfall of client and support messages
# where key - email
# key - (operator_name, client_email) ; value - [ {'who': 'operator', message: 'some'}, {'who': 'client', message: 'some2'},  ]
ws_dialog = {}

def addDialogMsg(operator_name, client_email, who_sended, message):
    ws_dialog[(operator_name, client_email)].append( { 'who': who_sended, 'message': message } )

callback_cmd_list = ['/urgent', '/install', '/other', '/market', '/rub', '/yuan', '/sup', '/pay']

def addWsConn(from_who, email_or_name, ws_conn):

    if from_who == 'operator':
        operator_ws[email_or_name] = ws_conn

    elif from_who == 'client':
        client_ws[email_or_name] = ws_conn

    else:
        raise Exception('from_who - unknown type')

all_commands = command_answers.keys()
print(all_commands)

