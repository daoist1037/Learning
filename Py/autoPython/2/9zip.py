import zipfile, os
examplezip = zipfile.ZipFile('a.zip')
print(examplezip.namelist())
ainfo = examplezip.getinfo('Python.pdf')
print(ainfo.file_size)
print(ainfo.compress_size)

examplezip.extractall('ceshi4')
examplezip.extract('hello.py', 'ceshi5')

newzip = zipfile.ZipFile('ceshi4\\new.zip', 'w')
newzip.write('Python.pdf', compress_type=zipfile.ZIP_DEFLATED)

examplezip.close()