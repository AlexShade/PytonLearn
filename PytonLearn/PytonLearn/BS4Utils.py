from bs4 import BeautifulSoup

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

	return errCode, errText, bs4Doc
