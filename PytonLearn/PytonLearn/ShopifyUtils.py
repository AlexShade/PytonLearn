from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
#Получть все товары

#Top 5 бестселлеров

#Получить товар по id
def getShopifyProduct(startULR, path):
    if (path.endswith("?view=quick")):
       path = path.replace("?view=quick", "");
    title = path.replace("/products/", "");

    response = urlopen(startULR+"/products/"+title+".js")
    data = json.loads(response.read())
    return data
