import numpy as np
import pandas as pd
import pywikibot

data=pd.read_csv("awgnz data final.csv",delimiter=";")
data3=data[['nb_hab','nb_fam','ar_name','shi_name','taqbilt','shi_taqbilt','nb_hab_2014','nb_fam_2014']]

SAVE_MESSAGE=''

site = pywikibot.Site()

f = open("article 1.txt", "r", encoding="utf8")
text1=str(f.read())
f = open("article 2 2014.txt", "r", encoding="utf8")
text2=str(f.read())
f = open("article 3.txt", "r", encoding="utf8")
text3=str(f.read())

for i in range(0,data3.shape[0]):
    print('*********'+str(i+1)+'/'+str(data3.shape[0])+'************* : '+str(data3['shi_name'][i]))
    name_final=data3['shi_name'][i]+' ('+data3['shi_taqbilt'][i]+')'
    page=pywikibot.Page(site,name_final)
    temp_text = page.text
    
    if temp_text=='':
    
        ar_name_awgnz = data3['ar_name'][i]+' ('+data3['taqbilt'][i]+')'
        text_adwwar=text1.replace('shi_name',data3['shi_name'][i]).replace('ar_name',ar_name_awgnz).replace('nb_fam',str(data3['nb_fam'][i])).replace('nb_hab',str(data3['nb_hab'][i])).replace('shi_taqbilt',data3['shi_taqbilt'][i])
        temp_text = text_adwwar
                
        if np.isnan(data3['nb_hab_2014'][i])==False:
            text_2014=text2.replace('nb_hab_2014',str(int(data3['nb_hab_2014'][i]))).replace('nb_fam_2014',str(int(data3['nb_fam_2014'][i])))
            temp_text = temp_text + text_2014
        
        temp_text = temp_text + text3.replace('shi_taqbilt',data3['shi_taqbilt'][i])
        
        if temp_text != page.text:
            page.text = temp_text
            page.save(SAVE_MESSAGE)
