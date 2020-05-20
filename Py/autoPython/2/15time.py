import time
def fac(a):
    num = 1
    for i in range(a):
        num *= i
    return num
start_time = time.time()
fac(9999)
end_time = time.time()
print(end_time-start_time)

for i in range(4):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)