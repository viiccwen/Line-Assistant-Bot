from .crawler import function, IFoodie, okgo, weather
from .button_mes import button

list_function = ["美食推薦", "景點推薦", "天氣預覽"]

list_city = ["台北市", "基隆市", "新北市", 
             "台中市", "桃園市", "台南市",
             "高雄市", "宜蘭縣", "新竹縣",
             "苗栗縣", "彰化縣", "南投縣",
             "雲林縣", "嘉義縣", "屏東縣",
             "台東縣", "花蓮縣", "新竹市","嘉義市"]


class Main:
    func = '0'

    def ChooseFunc(sentence):
        if Main.func == '0' and (sentence in list_function):
            if sentence == '美食推薦':
                Main.func = '1'
                return button()

            elif sentence == '景點推薦':
                Main.func = '2'
                return button()

            elif sentence == '天氣預覽':
                Main.func = '3'
                return button()

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

    def check(sentence):

        if (Main.func == '0') and (sentence in list_function):
            return '1'

        elif (Main.func != '0') and (sentence in list_city):
            return '2'

        else:
            return '0'