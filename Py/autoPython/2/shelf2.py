import shelve
shelf = shelve.open('mydata')
cat = ['zophie', 'Pooka', 'simon']
shelf['cats'] = cat
shelf.close()