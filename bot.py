import re

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# TOKEN = '8123973060:AAFKQ9HFsRiCAHBz4eSDzxHBUEqYcMu0klw'
TOKEN = '5244750152:AAHu4dBlmFQZ-lylmMIeTyl-m-Tp3RD_u9E'
bot_username = "freaky1488_bot"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Дароу')


@bot.message_handler()
def text_handler(message):
    chat_id = message.chat.id
    # print(message.text)
    # print( re.match(rf'@{bot_username},? +пошли *(нахуй)? *[@a-zA-Z0-9_]+', message.text) is not None )

    if re.match(rf'@{bot_username},? +пошли *(нахуй)? *[@a-zA-Z0-9_]+', message.text) is not None:
        msg = f"{message.text.split()[-1]} ПАШОЛ НАХУЙ!"
        bot.send_message(chat_id=chat_id, text=msg)

    elif "1488" in message.text:
        bot.send_message(chat_id=chat_id, text="УМОРА!11!!!1! ОН НАПИСАЛ 1488!!!!!!!!!!!!!!!!")
    elif re.match(rf".*[Гг][Оо][Йй][Дд][Аа].*", message.text) is not None:
        bot.reply_to(message, "КТО-ТО СКАЗАЛ ГОЙДА????????")


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
