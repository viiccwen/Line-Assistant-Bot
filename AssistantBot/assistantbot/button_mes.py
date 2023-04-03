from linebot.models import *


def button():
    message=TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='縣市選擇',
                    text='請選擇縣市',
                    actions=[
                        PostbackAction(
                            label='基隆市',
                            text='基隆市',
                            data='基隆市'
                        ),
                        PostbackAction(
                            label='台北市',
                            text='台北市',
                            data='台北市'
                        ),
                        PostbackAction(
                            label='新北市',
                            text='新北市',
                            data='新北市'
                        )
                    ]
                ),
                CarouselColumn(
                    title='縣市選擇',
                    text='請選擇縣市',
                    actions=[
                        PostbackAction(
                            label='桃園市',
                            text='桃園市',
                            data='桃園市'
                        ),
                        PostbackAction(
                            label='新竹市',
                            text='新竹市',
                            data='新竹市'
                        ),
                        PostbackAction(
                            label='苗栗縣',
                            text='苗栗縣',
                            data='苗栗縣'
                        )
                    ]
                )
            ]
        )    
    )

    return message