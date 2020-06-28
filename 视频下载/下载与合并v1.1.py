import requests
import threading
import easygui as t
import os

'''需要自己更改的变量'''
url = 'http://······/000000.ts' #视频流url
begin = 0                   #视频流(.ts)开始号
end = 33                   #视频流(.ts)结束号
long = 4                    #视频流号码变化长度 例如：下载00000.ts到11111.ts时，长度为5
path = 'F:\\'     #保存视频流（.ts）的路径

'''全局变量'''
lock = threading.Lock()     #只是定义一个锁
threads = []                #多线程存放进程
download_num = 0            #已下载视频流数量
undownloads = []            #没有下载列表


def thread_download_mp4(url,begin, end, long) :     #多线程下载视频流
    for i in range(begin, end) :
        url,i = get_url(url,long,i)
        t = threading.Thread(target=download_mp4, args=(url,i))  # 添加线程到线程列表
        threads.append(t)
        t.start()  # 启动线程
    for t in threads:
        t.join()
def get_url(url,long,i):            #按照规定生成url
    temp = url[::-1].split('.',1)
    url = temp[1][::-1]
    type = '.' + temp[0][::-1]
    i = str(i).zfill(long)  # 补全长度 long为4时，1补全为0001
    url = url[:-long] + str(i) + type
    return url,i
def download_mp4(url,i) :   #下载单个视频流
    global download_num
    name = str(i) + '.mp4'
    try:
        flag = 0
        f = open(path + name, 'rb')
        f.read()
        f.close()
        download_num += 1
    except:
        flag = 1
    if flag:
        print('正在下载：' + name)
        undownloads.append(name)
        response = requests.get(url)
        if response.status_code == 200 :
            f = open(path + name, 'wb')
            f.write(response.content)
            f.close()
            undownloads.remove(name)
            os.system('cls')
            download_num += 1
            print('正在下载列表：')
            for undownload in undownloads :
                print(undownload,end='\t')
            print('\n------------------------------------------------------------------------------------------------------------------------'
                  '\n\n' + name + '下载完成\t还有' + str(end - download_num) + '个没有下载完成')
            show_percnet(download_num, end)
        else :
            return
def show_percnet(num,total):    #显示已下载百分比
    percent = num / total * 100
    rank = int(percent) /10
    str = '<'
    for i in range(1,21) :
        if i/2 < rank :
            str += '■'
        else :
            str += '-'
    str += '>已下载%.2f%s'
    print(str % (percent,'%'))

def add_mp4(begin, end, long) : #合并视频流文件
    for i in range(begin, end) :
        i = str(i).zfill(long)
        name = str(i) + '.mp4'
        try :
            f = open(path + name, 'rb')
            data = f.read()
            p = open('move.mp4', 'ab')
            p.write(data)
            f.close()
            p.close()
        except :
            pass

def main(url, begin, end, long ,path) :    #显示界面
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    choices = ['下载视频','合并视频']
    choice = t.choicebox(msg='选择功能', title='', choices=choices)
    if choice :
        if choice == choices[0] :
            thread_download_mp4(url,begin, end, long)
            input('已下载完成，按任意键退出。')
        elif choice == choices[1] :
            add_mp4(begin, end, long)
            input('已合并完成，按任意键退出。')

if __name__ == '__main__' :
    main(url,begin,end,long,path)

