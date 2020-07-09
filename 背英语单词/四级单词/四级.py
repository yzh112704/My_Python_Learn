import re
import os
import random
types= {'n.':'名词','pron.':'代词','ad':'形容词/副词','num.':'数词','v.':'动词','aux.':'助动词','vi':'不及物动词','vt':'及物动词','art.':'冠词','prep.':'介词','conj.':'连词','int.':'感叹词'}
def remember_word():
    f = open('词库.txt','r',encoding='utf-8')
    words = f.readlines()
    f.close()
    num = open('count.txt', 'r', encoding='utf-8')
    counts = num.readlines()
    num.close()
    total = 4609
    count = 0
    while len(counts) + count != total:
        i = random.randint(1,4609)
        if str(i) + '\n' not in counts :
            word = words[i].replace('\n','')
            word_english = re.search('(\w+) \w+\..+',word)
            word_chinese = re.search('\w+ (\w+\..+)',word)
            print('\t\t\t\t' + word_english.group(1))
            input('\t\t\t1 认识     2 不认识')
            print('\t\t\t' + word_chinese.group(1))
            print('\n\n\n')
            for key, value in types.items():
                print(key, value)
            flag = input('\n\t\t\t再次确认\n\t\t\t1 认识     2 不认识')
            if flag == '2':
                f = open('不认识.txt', 'a+', encoding='utf-8')
                f.write(word_english.group(1) + '\t' + word_chinese.group(1) + '\n')
                f.close()
            else :
                f = open('认识.txt', 'a+', encoding='utf-8')
                f.write(word_english.group(1) + '\t' + word_chinese.group(1) + '\n')
                f.close()
            num = open('count.txt', 'a+', encoding='utf-8')
            num.write(str(i) + '\n')
            num.close()
            count += 1
            os.system('cls')
    input('\t\t\t恭喜你，已背完，按任意键退出！')


def remember_know():
    f = open('认识.txt', 'r', encoding='utf-8')
    words = f.readlines()
    f.close()
    counts = []
    st = ''
    while len(counts) != len(words):
        i = random.randint(0, len(words) - 1)
        if i not in counts :
            counts.append(i)
            word = words[i].replace('\n', '')
            word_english = re.search('(\w+)\t\w+\..+', word)
            word_chinese = re.search('\w+\t(\w+\..+)', word)
            print('\t\t\t\t' + word_english.group(1))
            flag = input('\t\t\t1 认识     2 不认识\n\t\t\t')
            print('\t\t\t' + word_chinese.group(1))
            print('\n\n\n')
            for key, value in types.items():
                print(key, value)
            if flag == '2':
                st += word + '\n'
            input(st)
            os.system('cls')
    input('\t\t\t已复习完，按任意键退出！')

def remember_unknow():
    f = open('不认识.txt', 'r', encoding='utf-8')
    words = f.readlines()
    f.close()
    counts = []
    st = ''
    print(len(counts),len(words))
    while len(counts) != len(words):
        i = random.randint(0, len(words) - 1)
        if i not in counts:
            counts.append(i)
            word = words[i].replace('\n', '')
            word_english = re.search('(\w+)\t\w+\..+', word)
            word_chinese = re.search('\w+\t(\w+\..+)', word)
            print('\t\t\t\t' + word_english.group(1))
            flag = input('\t\t\t1 认识     2 不认识\n\t\t\t')
            print('\t\t\t' + word_chinese.group(1))
            print('\n\n\n')
            for key, value in types.items():
                print(key, value)
            if flag == '2':
                st += word + '\n'
            input(st)
            os.system('cls')
    input('\t\t\t已复习完，按任意键退出！')

def main():
    flag = input('\t\t\t输入1\t背单词\n\t\t\t输入2\t复习认识单词\n\t\t\t输入3\t复习不认识单词')
    if flag == '1':
        os.system('cls')
        num = open('count.txt', 'r', encoding='utf-8')
        counts = num.readlines()
        num.close()
        percent = int(len(counts) / 4609 * 100000) / 1000
        print('已学习' + str(len(counts)) + '个单词。\n已完成' + str(percent) + '%')
        remember_word()
    elif flag == '2':
        os.system('cls')
        remember_know()
    elif flag == '3':
        os.system('cls')
        remember_unknow()
main()

