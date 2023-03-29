import pywikibot
from copy import deepcopy

WELC_TEMP = "{{Asbrrk}}"
SAVE_MESSAGE = "Asbrrk n usmras"

site = pywikibot.Site()

ARTICLE_NAMESPACE = 3

pool = site.allpages(namespace=ARTICLE_NAMESPACE)
pool_size = len(list(deepcopy(pool)))
print('Uṭṭun n ismrasn: '+str(pool_size))
i=1
for page in pool:

    print('*********'+str(i)+'/'+str(pool_size))
    temp_text = page.text

    if WELC_TEMP not in temp_text:
        if "{{Talɣa:Asbrrk}}" not in temp_text:
            if "REDIRECT" not in temp_text:
                if "redirect" not in temp_text:
                    temp_text = WELC_TEMP + '--~~~~ \n' + temp_text
                

    if temp_text != page.text: 
        page.text = temp_text
        page.save(SAVE_MESSAGE)
        
    i=i+1
