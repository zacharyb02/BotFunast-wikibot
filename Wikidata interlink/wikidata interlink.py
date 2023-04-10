import pywikibot
import numpy as np
import pandas as pd

data=pd.read_csv("Data_Awgnz_Idawgnidif_Wikidata.csv",delimiter=";")
data2=data[["ar_name","shi_name","taqbilt","shi_taqbilt"]]

site1 = pywikibot.Site("ar", "wikipedia")
site2 = pywikibot.Site("shi", "wikipedia")

site = pywikibot.Site("wikidata", "wikidata")

for i in range(0,data2.shape[0]):
    print('*********'+str(i+1)+'/'+str(data2.shape[0])+'************* : '+str(data2['shi_name'][i]))
    ar_article_name=str(data2["ar_name"][i]+" ("+data2["taqbilt"][i]+")")
    shi_article_name=str(data2["shi_name"][i]+" ("+data2["shi_taqbilt"][i]+")")

    repo = site.data_repository()
    page = pywikibot.Page(site1, ar_article_name)
    page_shi = pywikibot.Page(site2, shi_article_name)
    item = pywikibot.ItemPage.fromPage(page)
    page2 = pywikibot.Page(site2, shi_article_name)
    item.setSitelink(page2, summary=u'Adding shi article')
    print(shi_article_name,": Linked")
