from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
from linebot.models import *

from django.conf import settings

from .crawler import function, IFoodie, okgo, weather
from .button_mes import button
from .openai_mes import openai_module

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

list_function = ["美食推薦", "景點推薦", "天氣預覽", "AI對話"]

list_city = ["台北市", "基隆市", "新北市", 
             "台中市", "桃園市", "台南市",
             "高雄市", "宜蘭縣", "新竹縣",
             "苗栗縣", "彰化縣", "南投縣",
             "雲林縣", "嘉義縣", "屏東縣",
             "台東縣", "花蓮縣", "新竹市","嘉義市"]


class Main:
    func = '0'

    def ChooseOpenAI(sentence):
            ai_reply = openai_module(sentence)
            return ai_reply

    def ChooseFunc(sentence):
        if Main.func == '0' and (sentence in list_function):
            if sentence == '美食推薦':
                Main.func = '1'
                return button('美食推薦選單')

            elif sentence == '景點推薦':
                Main.func = '2'
                return button('景點推薦選單')

            elif sentence == '天氣預覽':
                Main.func = '3'
                return button('天氣預覽選單')
            
            elif sentence == 'AI對話':
                Main.func = '4'
                before_start_reply = "【AI對話已開啟...】\n\n點擊左下角即可開始打字聊天\n如需中斷請輸入「對話中斷」\n祝您聊天愉快。"
                return before_start_reply

        else:
            return []
        
    def ChooseArea(sentence):
        if (Main.func != '0') and (sentence in list_city):
            
            if Main.func == '1':
                Main.func = '0'
                return IFoodie().crawler(sentence)

            elif Main.func == '2':
                Main.func = '0'
                return okgo().crawler(sentence)

            elif Main.func == '3':
                Main.func = '0'
                return weather().crawler(sentence)

            else:
                Main.func = '0'
                return 'error'
        
        else:
            Main.func = '0'
            return 'error'

    def checkAI():

        return False

    def main(event, sentence):
        if Main.func == '4':
            if sentence == '對話中斷':
                Main.func = '0'
                reply = "【AI對話已關閉...】"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(reply))
            
            else: 
                reply = Main.ChooseOpenAI(sentence)
                line_bot_api.reply_message(event.reply_token, TextSendMessage(reply))

        elif (Main.func == '0') and (sentence in list_function):
            if sentence == "美食推薦" or sentence == "景點推薦" or sentence == "天氣預覽":
                City_message = Main.ChooseFunc(sentence)
                line_bot_api.reply_message(event.reply_token, City_message)

            elif sentence == "AI對話":
                reply = Main.ChooseFunc(sentence)
                line_bot_api.reply_message(event.reply_token, TextSendMessage(reply))

        elif (Main.func != '0') and (sentence in list_city):
            reply = Main.ChooseArea(sentence)
            line_bot_api.reply_message(event.reply_token, TextSendMessage(reply))

        else:
            return '0'