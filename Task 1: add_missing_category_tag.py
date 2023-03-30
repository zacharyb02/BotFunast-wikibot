import pywikibot
from copy import deepcopy

NO_CAT_TAG = "{{}}"
SAVE_MESSAGE = ""

site = pywikibot.Site()

ARTICLE_NAMESPACE = 0 

pool = site.allpages(namespace=ARTICLE_NAMESPACE)

pool_size = len(list(deepcopy(pool)))
print('Number of articles: '+str(pool_size))

i = 1

for page in pool:
    print('*********'+str(i)+'/'+str(pool_size))

    cat_count = len(list(page.categories()))

    temp_text = page.text

    if cat_count == 0:
        if NO_CAT_TAG not in temp_text:
            if "REDIRECT" not in temp_text:
                temp_text = NO_CAT_TAG + '\n' + temp_text
                

    if temp_text != page.text:
        page.text = temp_text
        page.save(SAVE_MESSAGE)
        
    i=i+1
