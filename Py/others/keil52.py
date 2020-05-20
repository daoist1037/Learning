#-*- encoding: UTF-8 -*-
"""
>	FileName:	keil52.py
>	Author:	daoist
>	Email:	1748624858@qq.com
>	Creat:	2020:05:02:14:01
"""
import os
import time
from multiprocessing.dummy import Pool
from threading import Thread

import bs4
import lxml.html
import requests


def work(u):
    time.sleep(0.5)
    url = u
    down_html = requests.get(url)
    down_lxml = lxml.html.fromstring(down_html.content)
    down_href = down_lxml.xpath("//div[@class='dlfile']/b/a/@href")
    if down_href == []:
        return
    down_text = down_lxml.xpath("//div[@class='dlfile']/b/a/text()")
    down_path = "D:\\下载\\课件\\单片机\\newfiles\\" + down_text[0]
    if os.path.isfile(down_path):
        return
    down_file = requests.get(down_href[0]).content
    with open(down_path, 'wb') as f:
        f.write(down_file)


url = "http://www.keil.com/download/list/c51.htm"
c51_html = requests.get(url=url)
c51_lxml = lxml.html.fromstring(c51_html.content)
lis = c51_lxml.xpath("//div[@class='Bdy']/ul/li")
urls = []
for li in lis:
    a_href = li.xpath("./a/@href")
    urls.append(a_href[0])

pool = Pool()
a = pool.map(work, urls)
pool.close()
pool.join()
