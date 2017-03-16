from BS4Utils import getAllLinks
from StringUtils import getSocialLink, getEmail, getEmailFromList, getSocialLinkFromList
from bs4 import BeautifulSoup
import os 
#import StartParameters
#import subprocess
from urllib.request import urlopen


#os.system('python StartParameters.py --skip 0 --take 10 --mongo 127.0.0.1')

html = urlopen("https://00babies.com/")
bsObj = BeautifulSoup(html.read(), 'html.parser')

#Получть чистый текст или исходник
#htmltext = bsObj.prettify()

allLinks = getAllLinks(bsObj)

#Бестселлеры
htmlBest = urlopen("https://00babies.com/")
bsObjBest = BeautifulSoup(htmlBest.read(), 'html.parser')
allBestLinks = getAllLinks(bsObjBest,"/product/")


email = getEmailFromList(allLinks)
facebook = getSocialLinkFromList("facebook.com",allLinks)
pinterest = getSocialLinkFromList("pinterest.com",allLinks)

for link in allLinks:
    print(link)

print("finish") 