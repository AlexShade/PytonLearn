domainPreffix = ['en','us','uk','de','in','gb','es','it','fr','se','ru','pt','au','nz'] #https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D1%8B_%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2

#Привести строку в читаемый вид (для ссылок email)
def normalizeWebString(source):
    source = source.strip(" \t\n").lower()
    return source

#Обрезать строку начиная с символа
def trunkStr(source,fchar):
    if source.find(fchar)>-1:
       return source[0:source.find(fchar)]
    return source
    

#Выдернуть ссылку на соцсеть
def getSocialLink(SocialNetwork, path):
    path = normalizeWebString(path)
    
    strpos = -1
    for preffix in domainPreffix:
        strpos=path.find(preffix+"."+SocialNetwork)
        if strpos>-1:
            break
    if strpos == -1:
        strpos=path.find(SocialNetwork)
    
    if strpos>-1:
        path = path[strpos:len(path)]
        path = "https://" + path
        return path
    else:
        return ""

#Выдернуть ссылку из листа
def getSocialLinkFromList(SocialNetwork, pathlist):
    for i in reversed(pathlist):
        reslink = getSocialLink(SocialNetwork,i)
        if reslink !="":
            return reslink
    return ""

#Выдернуть email
def getEmail(path):
    path = normalizeWebString(path)
    path=trunkStr(path,"?");
    path=trunkStr(path," ");
    strpos=path.find("mailto:")
    if strpos>-1:
        path = path[strpos+len("mailto:"):len(path)]
        return path
    else:
        return ""

#Выдернуть email из листа
def getEmailFromList(pathlist):
    for i in reversed(pathlist):
        reslink = getEmail(i)
        if reslink !="":
            return reslink
    return ""