""" import bs4,lxml
file = open('..\\html\\example.html')
text = file.read()
soup = bs4.BeautifulSoup(text,'lxml')
a = soup.select('#test-1')
b = a[0].getText()
print(b) """
import lxml.html
file = open('..\\html\\example.html')
text = file.read()
se = lxml.html.fromstring(text)
a = se.xpath('//div[start-with(@id,"text")]/text()')
for i in a:
    print(i)
