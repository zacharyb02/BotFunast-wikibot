import pywikibot
import numpy as np
import pandas as pd

data=pd.read_csv("Data_Awgnz_Idawgnidif_Wikidata.csv",delimiter=";")
data2=data[["ar_name","shi_name","taqbilt","shi_taqbilt"]]

SAVE_MESSAGE=""

site = pywikibot.Site("wikidata", "wikidata")

For i in range(0,data2.shape[0]):
    ar_article_name=str(data2["ar_name"][i]+" ("+data2["taqbilt"][i]+")")
    shi_article_name=str(data2["shi_name"][i]+" ("+data2["shi_taqbilt"][i]+")")
    source_wiki = pywikibot.Site("ar", "wikipedia")
    source_page = pywikibot.Page(source_wiki, ar_article_name)

    target_wiki = pywikibot.Site("shi", "wikipedia")
    target_page = pywikibot.Page(target_wiki, shi_article_name)

    if target_wiki.code not in source_page.interwiki:
        source_page.interwiki[target_wiki.code] = target_page.title()
        source_page.save(SAVE_MESSAGE)
        print("Interwiki link added to " + shi_article_name)
    else:
        print("Interwiki link already exists for " + shi_article_name)
