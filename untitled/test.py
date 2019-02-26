from bs4 import BeautifulSoup
info = []
with open('C:/Users/51311/Desktop/豆瓣.html','rb') as wb_data:
     Soup = BeautifulSoup(wb_data,'lxml')
     #获取网页信息
     # print(Soup)

     #元素位置信息
     #anony-sns > div > div.main > div > div.albums > ul > li:nth-child(1) > div > a > img
     #anony-movie > div.wrapper > div.main > div > ul > li:nth-child(1) > div.rating > i
     #anony-sns > div > div.main > div > div.albums > ul > li:nth-child(1) > a

     #获取元素位置
     images = Soup.select("#anony-sns > div > div.main > div > div.albums > ul > li > div > a > img")
     titles = Soup.select("#anony-sns > div > div.main > div > div.albums > ul > li > a")
     scores = Soup.select("#anony-movie > div.wrapper > div.main > div > ul > li > div.rating > i")
     #print(images,titles,scores,sep='\n-----------------------\n')


     #获取标签文本信息
     for image,title,score in zip(images,titles,scores):
          '''
           当一个标签有多个文本的时候，可以用stripped_strings,
           举例：'cate':'list(stripped_strings)
          '''
          data = {
               'image':image.get('src'),
               'title':title.get_text(),
               'score':score.get_text(),

          }
          #print(data)
          info.append(data)
          for i in info:
               if float(i['score'])>7:
                    print(i['title'],i['image'])