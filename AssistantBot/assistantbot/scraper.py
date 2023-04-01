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
            content += f"{title} - {stars}顆星 \n{address} \n\n"
                    
        return content




class okgo(function):
    def scrape(self, area):
        # okgo 玩全台灣
        url = "https://okgo.tw/Search.html?Page=1&kw=" + area + "&st=1"
        response = requests.get(url = url, headers = {"user-agent" : user_agent.random})
                
        soup = BeautifulSoup(response.content, "html.parser") 

        cards = soup.find_all('li', {'id': 'Search_Content_li'}, limit=10)
        content = ""
        for card in cards:
            web_address = card.find('a', {'class' : 'STopic'})

            url = "https://okgo.tw/" + web_address["href"]
            response = requests.get(url = url, headers = {"user-agent" : user_agent.random})

            soup = BeautifulSoup(response.content, "html.parser") 

            information = soup.find('div', {'class' : 'sec3 word Resize'})

            title = information.find('h2', {'style' : 'color:#40a0bf;'}).getText()

            zone_list = information.find('strong').find_all('a')
            zone = ""
            for zones in zone_list: zone += zones.text

            TransInfo = soup.find('div', {'id' : 'Buty_View_Traffic'}).getText()


            content += f"{title} - {zone}\n\n{TransInfo}\n\n"


        return content

class check:
    func = '0'
    area = ""

    def CheckIFoodie(sentence):
        for i in list_food_dic:
            pos = sentence.find(i)

            if pos != -1:
                for j in list_city:
                    pos = sentence.find(j)

                    if pos != -1:
                        check.func = '1'
                        check.area = sentence[pos:pos+3]
                        break
            
            if check.area != "":
                
                break
    
    def CheckOkgo(sentence):
        for i in list_play_dic:
            pos = sentence.find(i)

            if pos != -1:
                for j in list_city:
                    pos = sentence.find(j)

                    if pos != -1:
                        check.func = '2'
                        check.area = sentence[pos:pos+3]
                        break

            if check.area != "":
                break


    def main(sentence):
        check.func = '0'
        check.area = ''

        check.CheckIFoodie(sentence)
        if(check.func == '0'): check.CheckOkgo(sentence)
        if(check.func == '0'): pass
            

        if check.func == '0':
            content = "none"
        
        elif check.func == '1':
            content = IFoodie().scrape(check.area)
        
        elif check.func == '2':
            content = okgo().scrape(check.area)


        return content