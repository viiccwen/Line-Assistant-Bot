from linebot.models import *

message = []

def button(sentence):
    global message
    if message == []:
        message = TemplateSendMessage(
            alt_text = 'Carousel template',
            template = CarouselTemplate(
                columns = [
                    CarouselColumn(
                        title=sentence,
                        text='請選擇縣市',
                        actions=[
                            MessageAction(
                                label='基隆市',
                                text='基隆市'
                            ),
                            MessageAction(
                                label='台北市',
                                text='台北市'
                            ),
                            MessageAction(
                                label='新北市',
                                text='新北市'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=sentence,
                        text='請選擇縣市',
                        actions=[
                            MessageAction(
                                label='桃園市',
                                text='桃園市'
                            ),
                            MessageAction(
                                label='新竹縣',
                                text='新竹縣'
                            ),
                            MessageAction(
                                label='新竹市',
                                text='新竹市'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=sentence,
                        text='請選擇縣市',
                        actions=[
                            MessageAction(
                                label='苗栗縣',
                                text='苗栗縣'
                            ),
                            MessageAction(
                                label='台中市',
                                text='台中市'
                            ),
                            MessageAction(
                                label='彰化縣',
                                text='彰化縣'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=sentence,
                        text='請選擇縣市',
                        actions=[
                            MessageAction(
                                label='雲林縣',
                                text='雲林縣'
                            ),
                            MessageAction(
                                label='嘉義縣',
                                text='嘉義縣'
                            ),
                            MessageAction(
                                label='嘉義市',
                                text='嘉義市'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=sentence,
                        text='請選擇縣市',
                        actions=[
                            MessageAction(
                                label='台南市',
                                text='台南市'
                            ),
                            MessageAction(
                                label='高雄市',
                                text='高雄市'
                            ),
                            MessageAction(
                                label='屏東縣',
                                text='屏東縣'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=sentence,
                        text='請選擇縣市',
                        actions=[
                            MessageAction(
                                label='台東縣',
                                text='台東縣'
                            ),
                            MessageAction(
                                label='花蓮縣',
                                text='花蓮縣'
                            ),
                            MessageAction(
                                label='宜蘭縣',
                                text='宜蘭縣'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title=sentence,
                        text='請選擇縣市',
                        actions=[
                            MessageAction(
                                label='南投縣',
                                text='南投縣'
                            ),
                            MessageAction(
                                label='澎湖縣',
                                text='澎湖縣'
                            ),
                            MessageAction(
                                label='Not Implement',
                                text='Not Implement'
                            )
                        ]
                    )
                ]
            )    
        )

    return message