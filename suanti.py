import re
import random

name = input('Please input your name:')
f = open('tiku.txt','r',encoding='utf-8')
p = open(name+'.txt','w+',encoding='utf-8')
timu = f.read()
book = [0]*46
for i in range(5):
    if i == 4:
        num1 = random.randint(i*10+1,i*10+5)
    else:
        num1 = random.randint(i*10+1,(i+1)*10)
    if book[num1] == 0:
        print(num1,'\n')
        book[num1] = 1
        num2 = num1+1
        strs = re.search((str(num1)+'\. .*?') + str(num2) + '\.',timu,re.S)
        strs = strs.group(0)
        strs = re.sub('\s\d+\.$','',strs)
        p.write(strs+'\n')
        print(strs)
    else:
        i-=1
f.close()
p.close()