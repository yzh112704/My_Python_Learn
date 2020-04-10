import re
import os
import random
def main(nu):
    f = open('3.txt','r',encoding='utf-8')  #3.txt题库名称
    st = f.read()
    f.close()
    book = [0]*(nu+1)
    num = 1
    count_right = 0
    count_wrong = 0
    wrongs = []
    i = random.randint(1,nu)
    while True:
        print('判断题输入T（对）、F（错）。')
        s = re.search(str(i) + '\.(.*?)' + str(i+1) + '\.',st,re.S)
        kong = re.sub('（ *对 *）|（ *错 *）','（ ）',s.group(1))
        print(kong)
        n = input()
        #print(s.group(1))
        try :
            key = re.search('（ *(对) *）|（ *(错) *）',s.group(1))
            if key.group(1) == None :
                print('答案是：',key.group(2))
                if 'F' == n :
                    count_right += 1
                else:
                    count_wrong +=1
                    wrongs.append(s.group(1))
            else :
                print('答案是：',key.group(1))
                if 'T' == n :
                    count_right += 1
                else:
                    count_wrong += 1
                    wrongs.insert(0,s.group(1))
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
                return wrongs
        num += 1
        print('总共第' + str(num-1) + '道题。')
        input()
        os.system('cls')

wrongs = main(130)  #题目总数
print('题已答完！！\n错题如下:\n')
for wrong in wrongs:
    print(wrong)
input()
