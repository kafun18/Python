from bs4 import BeautifulSoup
import requests

url = 'https://gz.58.com/pingbandiannao/36199097499657x.shtml'
#basicinfo > div.infocard__container.haveswitch > div:nth-child(3) > div.infocard__container__item__main

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
#div.detail-title__info >

title = soup.title.text
price = soup.select('.infocard__container__item__main__text--price')[0].text.strip()
date = soup.select('div.detail-title__info__text')[0].text
area = soup.select('div.infocard__container__item__main > a')[0].text
    # basicinfo > div.infocard__container.haveswitch > div:nth-child(1) > div.infocard__container__item__main > span
# data = {
#         'title':soup.title.text,
#         'price':soup.select('#basicinfo span.infocard__container__item__main__text--price')[0].text,
#         'date':soup.select('div.detail-title__info > div:nth-of-type(1)').text,
#         'area':list(soup.select('div.infocard__container__item__main > a')[0].stripped_strings)
#        }
print(area)
