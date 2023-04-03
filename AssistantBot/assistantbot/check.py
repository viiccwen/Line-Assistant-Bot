from .crawler import function, IFoodie, okgo, weather
from .button_mes import button

list_city = ["台北市", "基隆市", "新北市", 
             "台中市", "桃園市", "台南市",
             "高雄市", "宜蘭縣", "新竹縣",
             "苗栗縣", "彰化縣", "南投縣",
             "雲林縣", "嘉義縣", "屏東縣",
             "台東縣", "澎湖縣", "新竹市","嘉義市"]


class check:
    func = '0'

    def main(sentence):
        content = ''

        if check.func == '0' and int(len(sentence)) == 4:
            if sentence == '餐廳美食':
                check.func = '1'
                return button()

            elif sentence == '旅遊景點':
                check.func = '2'
                return button()

            elif sentence == '天氣預覽':
                check.func = '3'
                return button()

            else:
                return []

        elif (check.func != '0') and (sentence in list_city) and ( int(len(sentence)) == 3 ):
            

            if check.func == '1':
                check.func = '0'
                content = IFoodie().crawler(sentence)

            elif check.func == '2':
                check.func = '0'
                content = okgo().crawler(sentence)

            elif check.func == '3':
                check.func = '0'
                content = weather().crawler(sentence)

            else:
                check.func = '0'
                return 'error'

        else:
            check.func = '0'
            return 'error'

        return content