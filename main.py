import telebot
import constants

bot = telebot.TeleBot(constants.TOKEN_NAME)


@bot.message_handler(content_types=['text'])
def send_message(message):
    bot.send_message(message.chat.id, "Бот работает")


bot.polling(none_stop=True)
