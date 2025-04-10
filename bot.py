import random
import re

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReactionTypeEmoji

TOKEN = '8123973060:AAFKQ9HFsRiCAHBz4eSDzxHBUEqYcMu0klw'
# TOKEN = '5244750152:AAHu4dBlmFQZ-lylmMIeTyl-m-Tp3RD_u9E'
bot_username = "freaky1488_bot"
bot = telebot.TeleBot(TOKEN, parse_mode=None)
last_10_messages = []
last_messages = []
admin_id = "1212560164"
reactions = [ReactionTypeEmoji(emoji) for emoji in ["💋", "🍓", "❤️‍🔥", "💯", "👍", "❤️", "😭", "🍾", "🎉", "💅"]]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Дароу')


# @bot.message_handler(content_types=['photo', 'audio', 'document', 'video'])
@bot.message_handler(content_types=['voice'])
def audio_reply(message):
    bot.reply_to(message, "Не могу сейчас слушать, текстом напиши")
    # bot.send_audio(admin_id, message.voice)




@bot.message_handler(content_types=['sticker'])
def sticker_reply(message):
    print(message)


@bot.edited_message_handler(func=lambda message: True)
def handle_edited_message(message):
    bot.reply_to(message, "А ЧО ЭТО МЫ ТАМ ИЗМЕНИЛИ??????")


@bot.message_handler()
def text_handler(message):
    # print(message.text)
    global last_10_messages
    chat_id = message.chat.id

    last_messages.append(message)
    if len(last_messages) > 100:  # Храним только последние 100
        last_messages.pop(0)

    if message.chat.type == 'supergroup' or message.chat.type == 'group':
        # print([msgg.from_user.id for msgg in last_10_messages])
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

    elif message.text == f'@{bot_username}':
        bot.reply_to(message, "Че звал, Сларк?")

    elif re.match(rf"@{bot_username}.*", message.text) is not None:
        bot.reply_to(message, "Отстань")

    elif "1488" in message.text:
        bot.send_message(chat_id=chat_id, text="УМОРА!11!!!1! ОН НАПИСАЛ 1488!!!!!!!!!!!!!!!!")

    elif re.match(rf".*[Гг][Оо][Йй][Дд][Аа].*", message.text) is not None:
        match = re.search(rf"[Гг][Оо][Йй][Дд][Аа]", message.text)
        goyda = message.text[match.start():match.end()]
        bot.reply_to(message, f"КТО-ТО СКАЗАЛ {goyda}???")
    elif "🙏" in message.text:
        r = random.randint(1, 4)
        photo = open(f'static/img/prayer{r}.png', 'rb')
        bot.send_photo(chat_id, photo)
        photo.close()
    elif message.text == "Заткнись":
        bot.send_message(chat_id, "Тебе надо пояснить как не стоит общаться в интернете, хуйлан?")
    else:
        random_hate = random.randint(1, 25)
        random_reaction = random.randint(1, 25)
        random_message = random.randint(1, 15)
        if random_hate == 1:
            user = bot.get_chat_member(chat_id, message.from_user.id).user
            bot.reply_to(message, f"{user.first_name}{' ' + user.last_name if user.last_name is not None else ''} высказался"
)
            bot.set_message_reaction(chat_id=chat_id, message_id=message.id, reaction=[ReactionTypeEmoji('👎')],
                                     is_big=False)
        if random_reaction == 1:
            r_emoji = random.choice(reactions)
            bot.set_message_reaction(chat_id=chat_id, message_id=message.id, reaction=[r_emoji],
                                     is_big=False)
        if random_message == 1:
            if len(last_messages) > 0:
                r = random.randint(0, len(last_messages)-1)
                bot.send_message(chat_id, last_messages[r].text)


if __name__ == "__main__":

    try:
        print("Бот запущен...")

        bot.add_edited_message_handler({
            'callback': handle_edited_message,
        })
        # bot.add_message_reaction_handler({
        #     'callback': handle_reaction,
        # })
        bot.polling(none_stop=True)
    except SystemExit:
        last_10_messages = []
