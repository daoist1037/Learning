import time
from multiprocessing.dummy import Pool
num = 1
def calc():
    global num
    num += 1

def cal():
    num = 1
    for i in range(8):
        num+=1

pool = Pool(3)
start = time.time()
result = pool.map(calc,'')
end = time.time()
print(end-start)

import threading
start = time.time()
for i in range(8):
    thread = threading.Thread(target=calc)
    thread.start()
end = time.time()
print(end-start)

start = time.time()
cal()
end = time.time()
print(end-start)
