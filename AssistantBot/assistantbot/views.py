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
 
from .main import *


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
                LineUserId = event.source.user_id
                LineUserName = line_bot_api.get_profile(LineUserId)
                if LineUserId not in UserName:
                    print(f"New User Name: {LineUserName.display_name}")
                    print(f"New User UID: {LineUserId}")
                    print(event.message.text)
                    NewUser = Main()
                    UserName[LineUserId] = NewUser
                
                print(f"User Name: {LineUserName.display_name}")
                print(f"User UID: {LineUserId}")
                print(event.message.text)
                UserName[LineUserId].main(event,event.message.text) 
                    
        return HttpResponse()
    else:
        return HttpResponseBadRequest()