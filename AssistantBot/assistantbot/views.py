from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
from linebot.models import *
 
from .main import Main


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 
 
@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)
            print(events)

        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):
                
                func = Main.check(event.message.text)
                
                if func == '0':
                    line_bot_api.reply_message(
                    event.reply_token, TextSendMessage("error"))

                elif func == '1': # 回傳選擇縣市之列表 (json list)
                    City_message = Main.ChooseFunc(event.message.text)
                    line_bot_api.reply_message(
                    event.reply_token, City_message)

                elif func == '2': # 回傳功能對應之結果 (字串)
                    reply = Main.ChooseArea(event.message.text)
                    line_bot_api.reply_message(
                    event.reply_token, TextSendMessage(reply))
                    

        return HttpResponse()
    else:
        return HttpResponseBadRequest()