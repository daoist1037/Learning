from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
# import re
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(),'lxml')
print(bsObj.h1)
# time.sleep(1)
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
html2 = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html2.read(),'lxml')
namelist = bsObj.findAll('span',{"class":"green"})
for name in namelist:
    print(name.get_text())
""" text = bsObj.findAll('div',{'id':'text'})
print(text[0].get_text()) 
# get_text()得到的是所有文本内容，会自动过滤掉其中的 Tag """



from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img",{"src":re.compile(r"../img\/gifts/img.*\.jpg")})

la =bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for i in la:
    print(i.attrs)
for image in images:
    print(image["src"])
    # image的所有属性
    print(image.attrs)



from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
someTags = bsObj.findAll(lambda tag: len(tag.attrs)==2)
for tag in someTags:
    print(tag.get_text())