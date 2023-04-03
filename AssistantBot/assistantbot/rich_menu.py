import requests
import json
from linebot import LineBotApi, WebhookHandler

LINE_CHANNEL_ACCESS_TOKEN = 'nTq1eQPMhkDzRMTFpq+pen1iDw3NUW/oRIMVDwgLQcnBMfLvANFNsOv348pGqk5K2Fvfc3RWeAXkvHCAMtj5VtwI20R0PQdZwgpfrPKI0CcVcrWbNRu3EGfcXUZQwmMI9FAI9R1PIf3U1JgexfCc6wdB04t89/1O/w1cDnyilFU='

token = LINE_CHANNEL_ACCESS_TOKEN

Authorization_token = "Bearer " + LINE_CHANNEL_ACCESS_TOKEN

headers = {"Authorization":Authorization_token, "Content-Type":"application/json"}



line_bot_api = LineBotApi(token)

rich_menu_id = 'richmenu-53a65095ae8d9a4189eee71089b0152c'




path = r'' # 只能執行一次!!

with open(path, 'rb') as f:
    line_bot_api.set_rich_menu_image(rich_menu_id, "", f)





req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/'+rich_menu_id,
                       headers=headers)
print(req.text)

rich_menu_list = line_bot_api.get_rich_menu_list()


# token : richmenu-53a65095ae8d9a4189eee71089b0152c

'''
body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "false",
    "name": "Menu",
    "chatBarText": "更多資訊",
    "areas":[
        {
          "bounds": {"x": 113, "y": 45, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "身體資訊"}
        },
        {
          "bounds": {"x": 1321, "y": 45, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "營養素"}
        },
        {
          "bounds": {"x": 113, "y": 910, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "吃"}
        },
        {
          "bounds": {"x": 1321, "y": 910, "width": 1036, "height": 762},
          "action": {"type": "message", "text": "運動gogo"}
        }
    ]
  }
'''