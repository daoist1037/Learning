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
