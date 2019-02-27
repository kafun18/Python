from bs4 import BeautifulSoup
import requests

url = 'https://gz.58.com/pingbandiannao/36199097499657x.shtml'
#basicinfo > div.infocard__container.haveswitch > div:nth-child(3) > div.infocard__container__item__main

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

def get_links_from(who_sells=0):
    urls = []
    list_view = 'https://gz.58.com/pbdn/{}/'.format(str(who_sells))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select('td.t a.t'):
        urls.append(link.get('href').split('?')[0])
        return urls
        #print(urls)

def get_views_from(url):
    id = url.split('/')[-1].strip('x.shtml')
    api = 'https://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api)
    views = js.text.split('=')[-1]
    return url
    #print(js.text)

def get_item_info(who_sells=0):
    urls = get_links_from(who_sells)
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
# title = soup.title.text
# price = soup.select('div.infocard__container__item__main > span')
# date = soup.select('div.detail-title__info > div:nth-of-type(1)')
# area = soup.select('div.infocard__container__item__main > a')
    # basicinfo > div.infocard__container.haveswitch > div:nth-child(1) > div.infocard__container__item__main > span
        data = {
            'title':soup.title.text,
            'price':soup.select('.infocard__container__item__main__text--price')[0].text.strip() if soup.find_all('span','infocard__container__item__main__text--price') else None,
            'date':soup.select('div.detail-title__info__text')[0].text if soup.find_all('div','detail-title__info__text') else None,
            'area':list(soup.select('div.infocard__container__item__main > a')[0].stripped_strings) if soup.find_all('div','infocard__container__item__main') else None,
            'cate':'个人' if who_sells == 0 else '商家',
            'views':get_views_from(url)
            }
        print(data)

#get_item_info(url)

#get_links_from(0)
#get_views_from(url)

get_item_info()