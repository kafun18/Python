from bs4 import BeautifulSoup
import requests

url = 'https://gz.58.com/pingbandiannao/36199097499657x.shtml'
#basicinfo > div.infocard__container.haveswitch > div:nth-child(3) > div.infocard__container__item__main

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
# title = soup.title.text
# price = soup.select('div.infocard__container__item__main > span')
# date = soup.select('div.detail-title__info > div:nth-of-type(1)')
# area = soup.select('div.infocard__container__item__main > a')

    data = {
        'title':soup.title.text,
        'price':soup.select('div.infocard__container__item__main > span')[0].text,
        'date':soup.select('div.detail-title__info > div:nth-of-type(1)')[0].text,
        'area':list(soup.select('div.infocard__container__item__main > a')[0].stripped_strings)
        }
    print(data)

get_item_info(url)