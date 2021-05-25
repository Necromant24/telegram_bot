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
        "/Оплата": { "answer": messages.pay_type, "commands": [("В рублях ₽ или в гривнах ₴",'/rub'), ("В юанях ¥", "/yuan"), ("Связаться с поддержкой",'/Связаться с поддержкой')]},
        "/Пробный период": { "answer": messages.trial_text, "commands":[("Оплата",'/Оплата'), ("Связаться с поддержкой",'/Связаться с поддержкой')]},
        "/Узнать больше": { "answer": "Узнайте как заблокировать рекламу, какие появились сервера и многое другое", "commands": [["Блог",'https://market.zgc.su/zgcvpnblog']]},
        "/Для Туркменистана":  { "answer": messages.turk, "commands":[("Сайт обслуживания",'https://tm.zgc.su/'), ("Как подключить?",'https://sites.google.com/view/zgcvpn/try?authuser=0')]},
        "/Сотрудничество": { "answer": messages.coop, "commands":[["Сделать предложение",'https://zgcvpn.ru/partnership']]},
        "/ZGC SHOP": { "answer": messages.shop, "commands":[("ZGC SHOP",'https://market.zgc.su/'), ("Связаться с поддержкой", '/market') ]},
        "/Связаться с поддержкой": { "answer": messages.coop, "commands":[("Первичная настройка", "/install"),("Другое", "/other"), ('ZGC SHOP','/market')]},



        "/urgent": {"answer": messages.first_install, "commands":[]},
        "/install": {"answer": messages.first_install, "commands":[]},
        "/other": {"answer": messages.support, "commands":[]},
        "/market": {"answer": 'Здравствуйте! Укажите, пожалуйста, продукт и вопросы по нему', "commands":[]},
        "/rub": {"answer": messages.rub_text, "commands":[]},
        "/yuan": {"answer": messages.yuan_text, "commands":[]},

    }

# после такой команты открывается еще и диалог с тех поддержкой
open_dialog_cmds = ["/market"]



viewed_cmds = [ "/Оплата", "/Пробный период", "/Узнать больше",  "/Для Туркменистана", "/Сотрудничество", "/ZGC SHOP", "/Связаться с поддержкой" ]

ws_email_wsClient = {}

def send_ws_msg(client_email, message):
    ws = ws_email_wsClient[client_email]

    return ws.send(message)

def add_ws_conn(email, ws):
    ws_email_wsClient[email] = ws
    print('added ws for - ' + email)

def remove_ws_conn(email):
    del ws_email_wsClient[email]



callback_cmd_list = ['/urgent', '/install', '/other', '/market', '/rub', '/yuan', '/sup', '/pay']

all_commands = command_answers.keys()
print(all_commands)

