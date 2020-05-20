import random, sys

for i in range(5):
    print(random.randint(1,10))
# 区间为左闭右闭
i=0
while i < 100:
    print(i)
    if(i == 20):
        sys.exit()
    i += 1