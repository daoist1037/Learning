# %%
import threading,time,random
def a():
    a=random.randint(1,10)
    a *= 10
    print(a)

threads = []
for i in range(8):
    thread = threading.Thread(target=a)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('Done')
# %%
#encoding=utf-8
import threading
import time

threadLock = threading.Lock()
num = 0
class timer(threading.Thread):
    def __init__(self, count, interval):
        threading.Thread.__init__(self)
        self.interval = interval
        self.count = count
    def run(self):
        global num
        while True:
            # 获得锁
            threadLock.acquire()
            if num >= self.count:
                # 释放锁
                threadLock.release()
                break
            num += 1
            print ('Thread name:{}, {}'.format(self.getName(), num))
            # 释放锁
            threadLock.release()

            time.sleep(self.interval)

if __name__ == '__main__':
    thread1 = timer(1000, 1)
    thread2 = timer(1000, 1)
    thread1.start()
    thread2.start()
    thread2.join()
    thread2.join()
