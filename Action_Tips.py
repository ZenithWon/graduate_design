import time

count=50

begin=time.time()
print('准备开始动作录入')

for i in range(3,0,-1):
    time.sleep(1)
    print(i,end=' ')

time.sleep(1)
print()
    
for i in range(1,count+1):
    print('第%i次动作' %i)
    time.sleep(3)
end=time.time()
print(end-begin)