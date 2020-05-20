import threading,time
threadobj = threading.Thread(target=print, args=['cats', 'dogs', 'frogs'], kwargs={'sep':' & '})
threadobj.start()
print('a')
# 并发问题