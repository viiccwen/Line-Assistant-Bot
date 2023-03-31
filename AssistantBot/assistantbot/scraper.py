from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from abc import ABC, abstractmethod
from lxml import etree, html

ua = UserAgent() 
user_agent = UserAgent()

list_city = ["台北市", "基隆市", "新北市", 
             "台中市", "桃園市", "台南市",
             "高雄市", "宜蘭縣", "新竹縣",
             "苗栗縣", "彰化縣", "南投縣",
             "雲林縣", "嘉義縣", "屏東縣",
             "台東縣", "澎湖縣", "新竹市","嘉義市"]

list_play_dic = ["景點", "好玩", "地方", "地點", "地", "娛樂"]

list_food_dic = ["餐廳", "好吃", "美食", "飲食", "吃飯"]

class function(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def scrape(self):
        pass


class IFoodie(function):
    def scrape(self, area):
        # IFoodie 愛食記網站
        url = "https://ifoodie.tw/explore/" + area + \
            "/list?sortby=popular&opening=true"
        
        response = requests.get(url = url, headers = {"user-agent" : user_agent.random})
                
        soup = BeautifulSoup(response.content, "html.parser")

        cards = soup.find_all('div', {'class': 'jsx-1156793088 restaurant-info'}, limit=10)
        print(len(cards))
        content = ""

        for card in cards:
                    
            title = card.find(  # 餐廳名稱
            "a", {"class": "jsx-1156793088 title-text"}).getText()

            stars = card.find(  # 餐廳評價
            "div", {"class": "jsx-2373119553 text"}).getText()
        
            address = card.find(  # 餐廳地址
            "div", {"class": "jsx-1156793088 address-row"}).getText()
        
        
            #將取得的餐廳名稱、評價及地址連結一起，並且指派給content變數
            content += f"{title} \n{stars}顆星 \n{address} \n\n"
                    
        return content




class okgo(function):
    def info(self, web_address):
        url = "https://okgo.tw/" + web_address

        response = requests.get(url = url, headers = {"user-agent" : user_agent.random})

        soup = BeautifulSoup(response.content, "html.parser") 

        information = soup.find('div', {'class' : 'sec3 word Resize'})

        title = information.find('h2', {'style' : 'color:#40a0bf;'}).getText()

        zones = information.find('strong').find_all('a')
        zone_text = ""
        for zone in zones: zone_text += zone.text

        #phone = information.find('h2')
        #print(len(phone))

        TransInfo = soup.find('div', {'id' : 'Buty_View_Traffic'}).getText()


        content = f"{title}\n\n{zone_text}\n\n{TransInfo}\n\n" #\n{phone}"#\n{address}
        return content

    def scrape(self, area):
        # okgo 玩全台灣
        url = "https://okgo.tw/Search.html?Page=1&kw=" + area + "&st=1"
        response = requests.get(url = url, headers = {"user-agent" : user_agent.random})
                
        soup = BeautifulSoup(response.content, "html.parser") 

        cards = soup.find_all('li', {'id': 'Search_Content_li'}, limit=5)
        content = ""
        for card in cards:
            web_address = card.find('a', {'class' : 'STopic'})
            content += okgo().info(web_address["href"])
                    
        return content

class check(function):
    def scrape(self):
        pass
    
    def checkFunc(self, sentence):
        function = '0'
        area = ""

        for i in list_food_dic:
            pos = sentence.find(i)

            if pos != -1:
                for j in list_city:
                    pos = sentence.find(j)

                    if pos != -1:
                        function = '1'
                        area = sentence[pos:pos+3]
                        #print(area)
                        break
            
            if area != "":
                break
            
        if function == '0':
            for i in list_play_dic:
                pos = sentence.find(i)

                if pos != -1:
                    for j in list_city:
                        pos = sentence.find(j)

                        if pos != -1:
                            function = '2'
                            area = sentence[pos:pos+3]
                            #print(area)
                            break

                if area != "":
                    break

        if function == '0':
            content = "none"
        elif function == '1':
            content = IFoodie().scrape(area)
        elif function == '2':
            content = okgo().scrape(area)


        return content



#sentence = "台中市有什麼好吃的？"
#reply = check().checkFunc(sentence)
#print(reply)


