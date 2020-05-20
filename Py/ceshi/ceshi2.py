import os,re
mo = re.compile(r'\w*\d+\w*')
num = 0
str = ''
list =[]
for folderName,subfolders,files in os.walk('D:\\study'):
    #print(str(os.path.basename(folderName)))
    str = str + ' ' +os.path.basename(folderName)
    list = list +[os.path.basename(folderName)]
    num = num +1
mmo = mo.findall(str)
num =0
'''
for i in mmo:
    print(i)
    num = num +1
'''
print(num)
for i in list:
    print(i)