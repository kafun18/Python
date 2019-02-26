import requests
from bs4 import BeautifulSoup
import time

#url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = ['https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#FILTERED_LIST'.format(str(i)) for i in range(30,1230,30)]

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36',
    'Cookie':'TART=%1%enc%3A7d8vXj94k%2F%2FvRkHKv9CLkU5qJSy8wqxgrF9ChUigThdMRI2Zfu%2BoPFBrKDa3534HkMrE3%2FXzZXs%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TAUnique=%1%enc%3AjKpSBCyygo65kmzcukmFa0IEwsxia7v4GdFCVn23jaU2jHwltRJPGQ%3D%3D; TASSK=enc%3AABg2NSr1nQ4GgXjd0HgekSV5ElTLV80JrjJIZJHoH0MNeSb4YSFN2k%2BkFOPiZ%2FO0TlJkY0uiahwqv5kZWGwZRagnKk5q735t%2BFl6dr964mTj5Oq56KX259AIvmbzYOS8MA%3D%3D; VRMCID=%1%V1*id.16631*llp.%2F-m16631-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title*e.1551627352487; _ga=GA1.2.822774364.1551022558; _smt_uid=5c72b9e0.44e50bbd; __gads=ID=26cdef2aeb365acb:T=1551022555:S=ALNI_MZt_GVN3vqlcyOxSwPb0KfvIZKK0w; ServerPool=C; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CCCUVOwnPers%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CSPMCWBPers%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7CCCUVOwnSess%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CSPMCWBSess%2C%2C-1%7C; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; roybatty=TNI1625!AK1Xaa08ODPBKwXk97Hlh3IaOyw7JQvvMIxjMosR%2BLWL3Yewqe9s%2Fu0Q0Rm0p3UJJB6lJAZNt8bJp4JqT3VZQUyjRjKjmLFEoTRG5T3taaJOlLwXNFWVgpsi2uV8YY4sVkP5iijOB2SO9GfzJmBHXO4RKwzjngTxeU4p1MOVb4md%2C1; _gid=GA1.2.359789118.1551197394; _gat_UA-79743238-4=1; SecureLogin2=3.4%3AAKckmsER8tskGVtVTPOM4yFvEzn7gPziuSlYlcB2cRAI4dIc4x%2FvGQlAWXqM4wtmDYk296wMtNkmg5o1TVN1mWtPNbHl6D8EstDJ%2FWAmPA9DdmOvyW6r3cLwFAXo8Zf6fSy7pXncMkW25%2BlUHDB3%2BGgym2dSwY1NeO%2FYjRafQdlK9kjUQqvYp9D7BnEreWebWhq9GGx0Q%2B%2B8S8eRhjSMo7w%3D; TAAuth3=3%3Ad56c12ef6c811fc0635da5dc3d3de35b%3AAECdgyjI3cszv9M945JpFmIW%2Flb3lZOr4GZla%2FuGPSXDEmxLiMhoIoe2sR%2FP0b5v%2By3w7YTi%2FrmcKtdxtNIUvv7bVFMNeLibVKHrtqkc2KBYFRPNJcSJnAAfwfoWPjwqu4gnbW9WKUzWyNiObWz2n8VnSu2zkYZz7XokkCwroqg2YvcUG5uZ%2B9sS6wUlfGbX8Q%3D%3D; TASession=%1%V2ID.3A99689633251296C6466F26D695D862*SQ.7*LP.%2FAttractions-g60763-Activities-New_York_City_New_York%5C.html*LS.MetaPlacementAjax*GR.2*TCPAR.31*TBR.90*EXEX.59*ABTR.64*PHTB.0*FS.15*CPU.87*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.8775FA1B8A246A112F74EF9C4656A14C*FA.1*DF.0*FLO.60763*TRA.true*LD.60763; TAUD=LA-1551022552437-1*RDD-1-2019_02_24*LG-174868878-2.1.F.*LD-174868879-.....'
}

def get_acctractions(url,data=None):
    wb_data = requests.get(url)
    time.sleep(4)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div.listing_title > a[target="_blank"]')
    imgs = soup.select('img[width="180"]')

    for title,img in zip(titles,imgs):
      data = {
            'title':title.get_text(),
            'img':img.get('src')
            # 'cate':list(cate.stripped_strings),
      }
      print(data)

for single_url in urls:
     get_acctractions(single_url)