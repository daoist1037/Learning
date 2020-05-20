import os,requests,re,time
from multiprocessing.dummy import Pool
star = time.time()
def calc(num) :
    time.sleep(1)
    ur = 'https://www.kanunu8.com/book3/6879/' + address[num]
    html_sstr = requests.get(ur).content.decode('GBK')
    b = re.compile(r'(<p>)(.*?)(</p>)',re.DOTALL)
    context = b.search(html_sstr)
    docx=context.group(2).replace('<br />','')
    docx=docx.replace('\r\n','\r')
    filename = '.\\pyscrapy\\zhuzhu\\chapter_No'+ str(num+1)+'.txt'
    file = open(filename,'w')
    file.write(docx)
    file.close()

html_str = requests.get('https://www.kanunu8.com/book3/6879/').content.decode('GBK')
a = re.compile(r'<a href="(\d+.html)')
address = a.findall(html_str)

origin_num = [x for x in range(len(address))]
# pool = Pool(len(address))
pool = Pool(10)
result = pool.map(calc, origin_num)

end = time.time()

print(end - star)