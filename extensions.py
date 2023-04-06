import requests
import json
from config import TOKEN, exchanges


class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base_key == quote_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')
        try:
            base_key == exchanges[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}!')
        try:
            quote_key == exchanges[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}!')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base{base_key}&symbols{quote_key}')
        resp = json.loads(r.content)
        new_price = resp['rates'][quote_key] * amount
        new_price = round(new_price, 3)
        text = f'Цена {amount} {base} в {quote} : {new_price}'

    bot.send_message(message.chat.id, text)


bot.polling()