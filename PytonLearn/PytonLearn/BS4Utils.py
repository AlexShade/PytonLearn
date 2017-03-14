from bs4 import BeautifulSoup

#Получть все ссылки с документа
def getAllLinks(bsObj):
    pages = list()
    for link in bsObj.findAll('a', href=True):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                pages.append(link.attrs["href"])
    return pages