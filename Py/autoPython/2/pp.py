import pprint
cats = [ {'name':'Zophie', 'desc':'chubby'}, {'name':'pokka', 'desc':'fluffy'}]
pprint.pformat(cats)
file = open('mycats.py', 'w')
file.write('cats = ' + pprint.pformat(cats) + '\n')
file.close()