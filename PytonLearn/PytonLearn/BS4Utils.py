from bs4 import BeautifulSoup

#получить ссылки со страницы
def getAllLinks(bsObj, containText = ""):
	pages = list()
	for link in bsObj.findAll('a', href=True):
		if "href" in link.attrs:
			if link.attrs["href"] not in pages:
				if (containText =="") or (str(link.attrs["href"]).find(containText)>-1):
					pages.append(link.attrs["href"])
	return pages