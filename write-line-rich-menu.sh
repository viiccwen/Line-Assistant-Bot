curl -v -X POST https://api.line.me/v2/bot/richmenu \
-H 'Authorization: Bearer {nTq1eQPMhkDzRMTFpq+pen1iDw3NUW/oRIMVDwgLQcnBMfLvANFNsOv348pGqk5K2Fvfc3RWeAXkvHCAMtj5VtwI20R0PQdZwgpfrPKI0CcVcrWbNRu3EGfcXUZQwmMI9FAI9R1PIf3U1JgexfCc6wdB04t89/1O/w1cDnyilFU=}' \
-H 'Content-Type: application/json' \
-d \
'{
    "size": {
      "width": 2500,
      "height": 1686
    },
    "selected": false,
    "name": "richmenu-demo-1",
    "chatBarText": "Line-Assistant-Bot-Rich-Line-Template",
    "areas": [
      {
        "bounds": {
          "x": 0,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "NotImplement",
          "text": "NotImplement"
        }
      },
      {
        "bounds": {
          "x": 833,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "NotImplement",
          "text": "NotImplement"
        }
      },
      {
        "bounds": {
          "x": 1666,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "NotImplement",
          "text": "NotImplement"
        }
      },
      "bounds": {
          "x": 0,
          "y": 843,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "餐廳美食",
          "text": "餐廳美食"
        }
      },
      {
        "bounds": {
          "x": 833,
          "y": 843,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "旅遊景點",
          "text": "旅遊景點"
        }
      },
      {
        "bounds": {
          "x": 1666,
          "y": 843,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "天氣預覽",
          "text": "天氣預覽"
        }
      }
   ]
}'