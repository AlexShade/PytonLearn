from BS4Utils import getAllLinks
from StringUtils import getSocialLink, getEmail, getEmailFromList, getSocialLinkFromList
from bs4 import BeautifulSoup
import os 
#import StartParameters
#import subprocess
from urllib.request import urlopen


os.system('python StartParameters.py --skip 0 --take 10 --mongo 127.0.0.1')

print(getSocialLink("facebook.com"," \" htttpss://facebook.com/boo\"   "))
print(getEmail("mailto:rshade@mail.ru  1?boo=null"))
print(getEmail("mailto:mailto:info@00babies.com"))


html = urlopen("https://00babies.com/")

bsObj = BeautifulSoup(html.read(), 'html.parser')
#htmltext = bsObj.prettify()

allLinks = getAllLinks(bsObj)
email = getEmailFromList(allLinks)
facebook = getSocialLinkFromList("facebook.com",allLinks)
pinterest = getSocialLinkFromList("pinterest.com",allLinks)

for link in allLinks:
    print(link)

print("finish") 