import threading,time,sys
def a():
    time.sleep(5)
    print('a')

threadobj = threading.Thread(target=a)
threadobj.start()

print('b')