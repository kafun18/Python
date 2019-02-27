#图片有些网站有反爬虫功能，可以尝试在手机端爬图片
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'

mb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(mb_data.text,'lxml')
imgs = soup.select('div.thumb.thumbLLR.soThumb > img')

for i in imgs:
    print(i.get('src'))