from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError

#get all links from bsObj
def getAllLinks(bsObj, startWith = ""):
	pages = list()
	if bsObj is None:
		return pages
	for link in bsObj.findAll('a', href=True):
		if "href" in link.attrs:
			if link.attrs["href"] not in pages:
				if (startWith =="") or (str(link.attrs["href"]).startswith(startWith)): #or (str(link.attrs["href"]).find(containText)>-1):
					pages.append(link.attrs["href"])
	return pages

#get bs4 doc
def getBS4Document(path):
	errCode = 0
	errText = ""
	try:
		html = urlopen(path)
		bsObj = BeautifulSoup(html.read(), 'html.parser')
	except URLError as e:
		if hasattr(e, 'code'):
			errCode = 1
			errText = e.code
		else:
			errCode = 2
			errText = "error"
	except:
		errCode = 3
		errText = "error"
	if errCode>0:
		bsObj =  BeautifulSoup('','html.parser')
	return errCode, errText, bsObj
