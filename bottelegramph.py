import telebot
import time

chave_api = "5394656938:AAGIHpWyklXhhTGzGuJvzwDowjXj8tCPlPc"
bot = telebot.TeleBot(chave_api)

contador = 0

while True:

    bot.send_message(953340214, f'Testando {contador}!')

    contador = contador + 1

    time.sleep(5)
