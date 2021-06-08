import telebot
import config
import sqlite3 as sql

galochka = "\U00002705"
msg_icon = "💬"

bot = telebot.TeleBot("493403387:AAGsQne6Pj0NTTQPwYo95gZ23jx5A2t59pw", parse_mode='HTML')


def db_find_value(col_name, value):
    """ Check if value exists in database and return corresponding row, 'col_name' must be name of DB column
        DB columns in order: email, date, tariff, sub, tg_id, vk_id, fb_id, state, rate, review_time, received, verified """

    with sql.connect(config.db_file) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM clients WHERE "+col_name+" = ?", (str(value).lower(),))
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

    message = "\U00002139\nemail: "+info[0]+"\n" \
              "date: "+info[1]+"\n" \
              "tariff: "+info[2]+"\n" \
              "sub: "+info[3]+"\n"

    return message


chat_id = 513268133

msg = """lorem ipsum dolor sit amet, 
lorem ipsum dolor sit amet, lorem ipsum dolor sit amet, lorem ipsum dolor 
sit amet, lorem ipsum dolor sit amet, lorem ipsum dolor sit amet,"""

message_data = "💬\n " + msg + "\n\n" + client_info_msg("email", 'lol@mail.ru') + "\nWeb_client"


bot.send_message(chat_id=chat_id, text= message_data)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    msg = "cleskdvd;svkj lkdjnv ;dkjnf kjdnf ;jndf kj;fnd klvnjd jnfb df;"
    message_data = "💬\n " + msg + "\n\n" + client_info_msg("email", 'lol@mail.ru') + "\nWeb_client"

    bot.reply_to(message, message_data)


#bot.polling()

