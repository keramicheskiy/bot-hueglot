import re

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# TOKEN = '8123973060:AAFKQ9HFsRiCAHBz4eSDzxHBUEqYcMu0klw'
TOKEN = '5244750152:AAHu4dBlmFQZ-lylmMIeTyl-m-Tp3RD_u9E'
bot_username = "freaky1488_bot"
bot = telebot.TeleBot(TOKEN, parse_mode=None)
last_10_messages = []


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Дароу')


@bot.message_handler()
def text_handler(message):
    print(message.text)
    global last_10_messages
    chat_id = message.chat.id

    if message.chat.type == 'group':
        print([msgg.from_user.id for msgg in last_10_messages])
        if len(last_10_messages) < 10:
            last_10_messages.append(message)
        elif len(last_10_messages) == 10:
            user_id = message.from_user.id
            if sum([1 for msg in last_10_messages if msg.from_user.id == user_id]) == 10:
                bot.reply_to(message, "Заткнись")
                last_10_messages = []
            else:
                last_10_messages.pop(0)
                last_10_messages.append(message)

    if re.match(rf'@{bot_username},? +пошли *(нахуй)? *[@a-zA-Z0-9_]+', message.text) is not None:
        msg = f"{message.text.split()[-1]} ПАШОЛ НАХУЙ!"
        bot.send_message(chat_id=chat_id, text=msg)

    elif f'@{bot_username}' in message.text:
        bot.reply_to(message, "Че звал, Сларк?")

    elif "1488" in message.text:
        bot.send_message(chat_id=chat_id, text="УМОРА!11!!!1! ОН НАПИСАЛ 1488!!!!!!!!!!!!!!!!")

    elif re.match(rf".*[Гг][Оо][Йй][Дд][Аа].*", message.text) is not None:
        match = re.search(rf"[Гг][Оо][Йй][Дд][Аа]", message.text)
        goyda = message.text[match.start():match.end()]
        bot.reply_to(message, f"КТО-ТО СКАЗАЛ {goyda}???")


if __name__ == "__main__":

    try:
        print("Бот запущен...")
        bot.polling(none_stop=True)
    except SystemExit:
        last_10_messages = []
