from bs4 import BeautifulSoup
import requests

# with open('C:/Users/kafun/Desktop/豆瓣.html','rb') as wb_data:
#     Soup = BeautifulSoup(wb_data,'lxml')
#     print(Soup)
'''
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('div.detail > div.item.name > a[target="_blank"]')
imgs = soup.select('img[width="200"]')
cates = soup.select('div.detail')

for title,img,cate in zip(titles,imgs,cates):
    data = {
        'title':title.get_text(),
        'img':img.get('src'),
        'cate':list(cate.stripped_strings),
    }
    print(data)
'''

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
    'Cookie':'CommercePopunder=SuppressAll*1551169858192; TASSK=enc%3AAMmi4QRmKtdGC6yTgyvnY%2Ft6mIkt5b8zGP4BxB4b2oJLKeDOnw2v0mtvG6SQrPVKJUJ1YSylhGQkNNBThzXrhKKp7x5KI5Nn5p1Zw8TIChFwUKUiQS4hyGiU5OwMUyoqEQ%3D%3D; TART=%1%enc%3AzEptQGq0LwMMdz9Vik9tr1C%2FLnSA1W%2BXsEVnwTAn0KbY3iWrfbwBlYH7uhJJMR2jS2LnoFsTfQg%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CCCUVOwnPers%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CSPMCWBPers%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7CCCUVOwnSess%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CSPMCWBSess%2C%2C-1%7C; TAUnique=%1%enc%3ARu4i8UpMjcbs9bpvqJbH5s0BWm%2B%2B9t0%2FbqG0jUni4r42jHwltRJPGQ%3D%3D; _ga=GA1.2.632397487.1551062157; _gid=GA1.2.2093469893.1551062157; __gads=ID=707ad759badb99cc:T=1551062159:S=ALNI_MbTcIUJXJuzLdc5ZnGBAsqLhIp-4w; TAAuth3=3%3Ab158ad518412013403c29fc3ed19c750%3AAEbEvnAkXGgjDf75CSbicaWP9u19LHmPpeIFWNHyO3bczjlBjBSVdA%2BNjdp%2BrJQ6apQ2ao5E9Utcdk%2F49rTX8JciXGERrPWiLOxrnWvodXPCVhSDSrfsj4axHWYk2T0NZD%2FwXMWa3sggV7%2BXktTkWwBeX8AyUpFpWJn7JGReVMYjaQ7DV0SxITExSgvdI%2BEcEQ%3D%3D; ServerPool=X; TAReturnTo=%1%%2FProfile; roybatty=TNI1625!AKbpsMyMG75J9SPKyK2XTxkOxjYSnw4dYVsaeSzEuyX3zLzvyzzqU66NY7M8RfryD7wuJsV5ggxL5Ksfs3fJqdQcvbACk%2BXc5r17Ly0I2Ns0mAG6kLgdRkYYAcSwUbw4k5B3AGRgWTcaBmz8YW6X59FePFUSW%2FA0y%2FOx%2Fpn35myj%2C1; TASession=%1%V2ID.509B27BF1B38F6FA6B5FD7D4765C9ECB*SQ.50*LP.%2FAttractions-g60763-Activities-New_York_City_New_York%5C.html*LS.DemandLoadAjax*GR.24*TCPAR.26*TBR.74*EXEX.5*ABTR.85*PHTB.44*FS.50*CPU.39*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.8775FA1B8A246A112F74EF9C4656A14C*FA.1*DF.0*FLO.60763*TRA.false*LD.4832685; TAUD=LA-1551062158589-1*RDD-1-2019_02_25*LG-109087179-2.1.F.*LD-109087180-.....'

}
url_Save = 'https://www.tripadvisor.cn/Saves/1550161'
wb_data = requests.get(url_Save,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('a.title')
#imgs = soup.select('div.media-left > a[url]')
#mates = soup.select('div.thumbnail')
print(soup)
#trip-item-collection-container > div.saves-item-card.card.is-fullwidth.hover > div > div.saves-location-details.ui_media > div.media-content > div > a
#trip-item-collection-container > div:nth-child(1) > div > div.saves-location-details.ui_media > div.media-left > a
# for title,mate in zip(titles,mates):
#     data={
#         'title':title.get_text(),
#         'mate':list(mate.stripped_strings)
#     }
# print(title)



