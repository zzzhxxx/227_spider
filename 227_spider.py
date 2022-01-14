# coding:utf-8
import requests
from bs4 import BeautifulSoup
# headers = {'Accept': ' */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,en-US;q=0.8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 jinjiedao'}
# spider
url="https://nanabunnonijyuuni.com/s/n129/diary/event/list"
data=requests.get(url)
bs=BeautifulSoup(data.text,"html.parser")
event_list=bs.find_all('div',class_="event_title")
event=[]
for i in event_list:
    title=i.text
    event.insert(0,title)
event_date=bs.find_all('div',class_="event_date_detail")
date=[]
for i in event_date:
    dat=i.text
    date.insert(0,dat)

#end
# print(data.text,encoding="gbk")
# with open('url.txt','w') as f:
#     f.write(event .encode('GBK','ignore').decode('GBK'))