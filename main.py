import telebot
import constants
from authorisation import get_marks

bot = telebot.TeleBot(constants.TOKEN_NAME)


@bot.message_handler(commands=["start", "help"])
def send_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать в бота, введите логин и пароль от БРС через пробел, "
                                      "чтоб узнать свои баллы")


@bot.message_handler(content_types="text")
def send_marks(message):
    bot.send_message(message.chat.id, "Данные получены, ожидайте ответа")
    bot.send_message(message.chat.id, get_marks(message.text))


bot.polling(none_stop=True)
