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
        "Оплата": { "answer": messages.pay_type, "commands": ["В рублях ₽ или в гривнах ₴", "В юанях ¥", "Связаться с поддержкой"]},
        "Пробный период": { "answer": messages.trial_text, "commands":["Оплата", "Связаться с поддержкой"]},
        "Узнать больше": { "answer": "Узнайте как заблокировать рекламу, какие появились сервера и многое другое", "commands": ["Блог"]},
        "Для Туркменистана":  { "answer": messages.turk, "commands":["Сайт обслуживания", "Как подключить?"]},
        "Сотрудничество": { "answer": messages.coop, "commands":["Сделать предложение"]},
        "ZGC SHOP": { "answer": messages.shop, "commands":["ZGC SHOP", "Связаться с поддержкой" ]},
        "Связаться с поддержкой": { "answer": messages.coop, "commands":[("Сделать предложение", "sldkoi"),("Срочная связь", "erihjoeir")]},
    }


all_commands = command_answers.keys()
print(all_commands)