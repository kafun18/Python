#异步获取元素信息
from bs4 import BeautifulSoup
import requests

url = 'https://download.csdn.net'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
imgs = soup.select('dt > a > img')
titles = soup.select('dd > a.album_detail_title')

for title,img in zip(titles,imgs):
            data = {
                'title':title.get_text().strip(),
                'img':img.get('src')
            }
            print(data)
