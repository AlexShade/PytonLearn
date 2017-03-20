from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import html2text

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

#find theme
def findTheme(html):
	stringForFind = "Shopify.theme = {\"name\":\""
	currPosition = html.find(stringForFind)
	if currPosition > 0:
		html = str(html)[currPosition+len(stringForFind):currPosition + 200 + len(stringForFind)]
	else:
		return ""
	currPosition = html.find("\"")
	if currPosition > 0:
		html = str(html)[0:currPosition]

	return html

#find currency
def findCurrency(html):
	stringForFind = "window.ShopifyAnalytics.meta.currency = "
	currPosition = html.find(stringForFind)
	if currPosition > 0:
		return html[currPosition+len(stringForFind)+1:currPosition+len(stringForFind)+4]
	else: return ""

#update ProductData
def updateProductData(targetCollection, ShopId, data, rank):
	productData = targetCollection.find( { "shopId": ShopId, "productId": data["id"] } )
	data["description"] = html2text.html2text(data["description"])

	if productData.count() == 0:
		#insert
		doc = {
			"shopId" : ShopId,
			"productId" : data["id"],
			"data" : data,
			"rank" : rank
			 }
		targetCollection.insert(doc)
	else:
		#update
		objectId = productData.next()
		targetCollection.update({"_id" : objectId["_id"] },
		 {"shopId" : ShopId,
		  "productId" : data["id"],
		  "data" : data,
		  "rank" : rank
		 }
		 )
	return
#update Shop
def updateData(targetCollection, target):
	targetCollection.update(
		{ "_id": target["_id"]},
		 {"scrapperResult" : target["scrapperResult"],
		  "Domain" : target["Domain"],
		  "StartURI" : target["StartURI"],
		  "scrapperResult" : target["scrapperResult"],
		  "currency" : target["currency"],
		  "theme" : target["theme"],
		  "email" : target["email"],
		  "instagramm" : target["instagramm"],
		  "facebook" : target["facebook"],
		  "twitter" : target["twitter"],
		  "pinterest" : target["pinterest"],
		  "youTube" : target["youTube"],
		  "google" : target["google"]
		  }	
		 )
	return