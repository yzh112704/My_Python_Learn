import re
import os
import random
def main(nu):
    f = open('1.txt','r',encoding='utf-8')  # 1.txt为题库名称
    st = f.read()
    f.close()
    book = [0]*(nu+1)
    num = 1
    count_right = 0
    count_wrong = 0
    i = random.randint(1,nu)
    i = 290
    while True:
        s = re.search('(' + str(i) + '\..*?)' + str(i+1) + '\.',st,re.S)
        kong = re.sub('（ *[A-F] *）','（ ）',s.group(1))
        kong = re.sub('_*[A-F]_', '___',kong)
        print(kong)
        n = input()
        #print(s.group(1))
        try :
            key = re.search('（ *([A-F]) *）|_*([A-F])_',s.group(1))
            if key.group(1) == None :
                print('答案是：',key.group(2))
                if key.group(2) == n :
                    count_right += 1
                else:
                    count_wrong +=1
            else :
                print('答案是：',key.group(1))
                if key.group(1) == n :
                    count_right += 1
                else:
                    count_wrong += 1
        except :
            pass
        book[i] = 1
        while book[i] :
            i = random.randint(1,nu)
            if num == nu :
                input()
                os.system('cls')
                print('总共' + str(num) + '道题。')
                print('总共' + str(num - count_right - count_wrong) + '道无效题。')
                print('答对' + str(count_right) + '道题。')
                print('答错' + str(count_wrong) + '道题。')
                return num
        num += 1
        print('总共第' + str(num-1) + '道题。')
        input()
        os.system('cls')
main(301)   #题目总数
input('题已答完！！')
