import telebot

bot = telebot.TeleBot('1545031066:AAEItl_xPAFS4Rc-gHVOWLIKcu11h5Kqe-g')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, Андрей")
    elif message.text == "привет":
        bot.send_message(message.from_user.id, "привет, Андрей")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Эй ты, напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)

