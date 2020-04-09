from bs4 import BeautifulSoup
from request import request
from filter import isMatch


def entries(page=1):
    arr = []
    r = request(page)
    print('page number is : ' + str(page))
    soup = BeautifulSoup(r.content, 'html5lib')
    list = soup.find_all(id="entry-item-list")
    for i in list:
        for child in i.findChildren("div", class_="content", recursive=True):
            temp = child.get_text().strip()
            if isMatch(temp):
                arr.append(rep(temp))
        return arr

def rep(entry):
    return entry.replace("#","");