#异步获取元素信息
from bs4 import BeautifulSoup
import requests
import time

url = 'ttps://download.csdn.net/index.php/source/ajax_get_more_code?pageno='
url1 = '&pagesize=10'
def get_page(url,data=None):
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        imgs = soup.select('dt > a > img')
        titles = soup.select('dd > a.album_detail_title')

        if data==None:
            for title,img in zip(titles,imgs):
             data = {
                'title':title.get_text().strip(),
                'img':img.get('src')
              }
             print(data)
def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one)+url1)
        time.sleep(2)

get_more_pages(4,1)