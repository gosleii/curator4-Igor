import telebot

bot = telebot.TeleBot('6955461632:AAE_Nfp0C-rSYqqoWGZrx9M76HquNQptAGE')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сообщение', parse_mode='Markdown')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, 'Побежали!!!\nБеги!!! *БЕГИ!!!*', parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'Это [Ссылка](https://pastebin.com/)', parse_mode='Markdown')


bot.infinity_polling()
