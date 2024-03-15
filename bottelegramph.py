import MetaTrader5 as mt5
import time
from telethon import TelegramClient, events
import logging
from telethon.sessions import StringSession
import telebot

import streamlit as st

st.title("Replicador de Mensagem do Telegram")


chave_api = "5394656938:AAGIHpWyklXhhTGzGuJvzwDowjXj8tCPlPc"
bot = telebot.TeleBot(chave_api)



def manipular_mensagem(event):


    texto = event.upper()
    texto = texto.split()

    remover = ['▪️USE','(@', 'Take', 'profit', '1', '3', '2', 'at', 'Stop', 'loss', ')', 'TAKE', 'PROFIT', 'AT', 'STOP',
               'LOSS', '-', 'tp1:', 'tp2:', 'tp3:', 'sl', ':', 'TP1:', 'TP2:','TP3:', 'SL','Entry', 'price:','price','Take','Stop', 'loss:','loss' ,'▪️', 'USE','MONEY','MANAGEMENT','2-3%', 'TP:','@', '(SWING)','(SCALPER)','(INTRADAY)','SL:']
    
    result = [palavra for palavra in texto if palavra not in remover]
    

    print(result)


def bot_encaminhar():
    #logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

    APP_ID = 17391157
    API_HASH = "82945fc118e2880f151e7ae587db7240"
    FROM_= [-1001436688109,-1001541343432] #id teste GRUPO RECEPTOR: -1001683021999 CLEVERPIP: -1001319789685 -1001436688109
    TO_= "953340214"
    SESSION = "1AZWarzgBu0PjvHH0RHfLLwXS0abkNJCJZopmx5CbExLrKwyd99Ns0xv-FcU0PCxlE0i3B_Dep-taoXoKfYlXPz2OHWZcDTZnAULvycm89lc_89SAeLqU5VmFdS3lHkZV6sBxDrNtLo2nmEb9lY-jYCZUy-Fjt-6oJbLJSckrrMlYqz4tV5fGLqwBfmqZqzna-KooJzhBoxoTka_Ao3tUsmE_qulzV1TOqLKnqG8B2oLaKrTL0ciz-PfF7I7MSxzI4R65ZiDITmXWsJHwXNJbnuu54O7SW9oHLGqg0uMabUZDFGrKpPBKmwGRqNY3udPHrfxCuD2LGrzRVk7RKpESXBd3S_OLE_A="

    FROM = FROM_

   # FROM = [int(i) for i in FROM_.split()]
    TO = [int(i) for i in TO_.split()]

    

    try:
        BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
        BotzHubUser.start()
    except Exception as ap:
        print(f"ERROR - {ap}")
        exit(1)

    @BotzHubUser.on(events.NewMessage(chats=FROM))
    async def sender_bH(event):

        event = event.message
        event = event.message

        bot.send_message(TO,event)

        #manipular_mensagem(event)
    print("Bot has started.")
    BotzHubUser.run_until_disconnected()
    
bot_encaminhar()
