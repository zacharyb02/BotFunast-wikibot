import numpy as np
import pandas as pd
import pywikibot

site = pywikibot.Site()

SAVE_MESSAGE="Talɣa n iḍwwaṛn n tgrawt"

data=pd.read_csv("Idawgnidif Data.csv",delimiter=";")
data3=data[["nb_hab","nb_fam","shi_name","ar_name","taqbilt","shi_taqbilt","tagrawt","shi_tagrawt","nb_hab_2014","nb_fam_2014"]]
data3

tagrawt=data3["shi_tagrawt"][0]

f = open("template header tagrawt.txt", "r", encoding="utf8")
text1=str(f.read())
f = open("template taqbilt d idwwarn.txt", "r", encoding="utf8")
text2=str(f.read())
f = open("template footer.txt", "r", encoding="utf8")
text3=str(f.read())

text_final=""
text_final=text1.replace("shi_tagrawt",data3["shi_tagrawt"][0])

index_change_taqbilt=[0]

adwwar_final=""
for i in range(0,data3.shape[0]):
    adwwar="[["+data3["shi_name"][i]+" ("+data3["shi_taqbilt"][i]+")|"+data3["shi_name"][i]+"]] · "
    adwwar_final=adwwar_final+adwwar
    if i!=data3.shape[0]-1:
        if data3["shi_taqbilt"][i+1] != data3["shi_taqbilt"][i]:
            adwwar_final=adwwar_final+"********************"
            index_change_taqbilt.append(i+1)
            
idwwarn=adwwar_final.split("********************")

for j in range(0,len(index_change_taqbilt)):
    text_final=text_final+"\n"+text2.replace("shi_tagrawt",data3["shi_tagrawt"][0]).replace("shi_taqbilt",data3["shi_taqbilt"][index_change_taqbilt[j]]).replace("shi_idwwarn",idwwarn[j][:-3])
                                        
text_final=text_final+"\n"+text3
temp_text=text_final
    
name_page="Talɣa:Iḍwwaṛn n Idaw Ggʷniḍif"
page=page=pywikibot.Page(site,name_page)

if temp_text != page.text:
            page.text = temp_text
            page.save(SAVE_MESSAGE)
