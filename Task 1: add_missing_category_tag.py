import pywikibot
from copy import deepcopy #to make deep copies instead of shallow copies

#!!!!!!!!!!MUST BE FILLED!!!!!!!!!
NO_CAT_TAG = "{{Amnni_ur_iṭṭafn_taggayt}}"
SAVE_MESSAGE = "Tamrniwt n tlɣa n imnnitn mi ixwa udɣar n tggayin"

#use the default site defined in user-config.py
site = pywikibot.Site()

ARTICLE_NAMESPACE = 0 #articles

#get all pages in the chosen namespace
pool = site.allpages(namespace=ARTICLE_NAMESPACE)

pool_size = len(list(deepcopy(pool))) #number of articles
print('Number of articles: '+str(pool_size))

i = 1

for page in pool:
    #keep track of processed pages
    print('*********'+str(i)+'/'+str(pool_size))

    #number of categories the page has
    cat_count = len(list(page.categories()))

    temp_text = page.text #temporary variable to store the page text

    if cat_count == 0: #page has no categories
        if NO_CAT_TAG not in temp_text: #page does not have the NO_CAT_TAG
            #adding NO_CAT_TAG to the text at the top
            if "REDIRECT" not in temp_text:
                temp_text = NO_CAT_TAG + '\n' + temp_text
                

    if temp_text != page.text: #if the text of the page has been changed by removing or adding the tag
        #update the text of the page
        page.text = temp_text
        #save to wiki
        page.save(SAVE_MESSAGE)
        
    i=i+1
