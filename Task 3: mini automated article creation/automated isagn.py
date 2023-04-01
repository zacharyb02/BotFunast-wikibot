import numpy as np
import pandas as pd
import pywikibot

SAVE_MESSAGE=""

data=pd.read_csv("final_data_awgnz.csv",delimiter=";")
data2=data[["nb_hab","nb_fam","name","ar_name"]]
data3=data2[0:26]
data3

site = pywikibot.Site()

f = open("example.txt", "r", encoding="utf8")
text=str(f.read())

for i in range(0,data3.shape[0]):
    print('*********'+str(i+1)+'/'+str(data3.shape[0])+'************* : '+str(data3['name'][i]))
    name_isagn=data3['name'][i]+' (Isagn)'
    page=pywikibot.Page(site,name_isagn)
    temp_text = page.text
    
    if temp_text=='':
    
        ar_name_awgnz = data3['ar_name'][i]+' (إساكن)'
        text_adwwar=text.replace('shi_name',data3['name'][i]).replace('ar_name',ar_name_awgnz).replace('nb_fam',str(data3['nb_fam'][i])).replace('nb_hab',str(data3['nb_hab'][i]))
        temp_text = text_adwwar
        
        if temp_text != page.text:
            page.text = temp_text
            page.save(SAVE_MESSAGE)
        
