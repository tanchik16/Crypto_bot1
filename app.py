import traceback
import telebot
from config import TOKEN, exchanges
from extensions import APIException, Convertor

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество валюты>\nВыведите список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanges.keys():
        text = '\n'.join((text, i, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    try:
        if len(values) != 3:
            raise APIException ('Неверное количество параметров!')
        answer = Convertor.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f'Ошибка в команде:\n(e)')
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f'Неизвестная ошибка:\n(e)')
    else:
        bot.reply_to(message, answer)

bot.polling()


