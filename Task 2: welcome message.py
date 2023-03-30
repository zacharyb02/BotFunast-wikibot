import pywikibot
from copy import deepcopy

WELCOME = "{{Asbrrk}}"
SAVE_MESSAGE = "Asbrrk n usmras"

ACTIF_USERS=['BotFunast']

site = pywikibot.Site()

ARTICLE_NAMESPACE = 3

last_changes = site.recentchanges(reverse=False,bot=False)

LAST_CONTR=[]
for item in last_changes:
    if item['user'] not in ACTIF_USERS:
        LAST_CONTR.append(item['user'])

LAST_CONTR = list(dict.fromkeys(LAST_CONTR))

i=1
pool_size = len(list(deepcopy(LAST_CONTR)))
print('Number of users: '+str(pool_size))

for contributor in LAST_CONTR:
    print('*********'+str(i)+'/'+str(pool_size))
    
    user = pywikibot.User(site,contributor)
    user_talk_page = user.getUserTalkPage()
    if user_talk_page.text == "":
        user_talk_page.text = WELCOME + '--~~~~'
        user_talk_page.save(SAVE_MESSAGE)

    else:
        temp_text = user_talk_page.text
        if WELCOME not in temp_text:
            if "{{Talɣa:Asbrrk}}" not in temp_text:
                if "REDIRECT" not in temp_text:
                    if "redirect" not in temp_text:
                        temp_text = WELCOME + '--~~~~ \n' + temp_text
        
        if temp_text != user_talk_page.text: 
            user_talk_page.text = temp_text
            user_talk_page.save(SAVE_MESSAGE)
    
    i=i+1
