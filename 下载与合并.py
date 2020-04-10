import os
import requests
import threading
import easygui as t
lock = threading.Lock()     #只是定义一个锁
threads = []
class Input_num():
    def __init__(self,begin = 0,end = 299,long = 3,path = os.getcwd(),url1 = '',url2 = ''):
        self.begin = begin
        self.end = end
        self.long = long
        self.path = path
        self.url1 = url1
        self.url2 = url2
class Download(Input_num):
    def __init__(self,url1,url2):
        Input_num.__init__(self)
        self.url1 = url1
        self.url2 = url2
    def thread_download_mp4(self) :
        isExists = os.path.exists(self.path + '\\视频流')
        if not isExists:
            os.makedirs(self.path + '\\视频流')
        for i in range(self.begin, self.end) :
            i = str(i).zfill(self.long)
            url = self.url1 + str(i) + self.url2
            t = threading.Thread(target=Download.download_mp4, args=(self,url,i))  # 添加线程到线程列表
            threads.append(t)
            t.start()  # 启动线程
        for t in threads:
            t.join()
    def download_mp4(self,url,i) :
        name = str(i) + '.mp4'
        try:
            flag = 0
            f = open(self.path + '\\视频流\\'+ name, 'rb')
            f.read()
            f.close()
            print(name + '已下载')
        except:
            flag = 1
        if flag:
            print('正在下载：' + name)
            response = requests.get(url)
            if response.status_code == 200 :
                f = open(self.path + '\\视频流\\'+ name, 'wb')
                f.write(response.content)
                f.close()
                print(name + '下载完成')
            else :
                return
class Add_mp4(Input_num) :
    def __init__(self,url1,url2):
        Input_num.__init__(self)
        self.url1 = url1
        self.url2 = url2
    def hebing(self):
        for i in range(self.begin, self.end):
            i = str(i).zfill(self.long)
            name = str(i) + '.mp4'
            try:
                f = open(self.path + '\\视频流\\'+ name, 'rb')
                data = f.read()
                p = open(self.path + '\\move.mp4', 'ab')
                p.write(data)
                f.close()
                p.close()
            except:
                pass
if __name__ == '__main__' :
    a = Input_num(url1 = '',url2 = '.ts')
    choices = ['下载视频', '合并视频']
    choice = t.choicebox(msg='选择功能', title='', choices=choices)
    if choice:
        if choice == choices[0]:
            b = Download(url1= a.url1,url2=a.url2)
            b.thread_download_mp4()
        elif choice == choices[1]:
            b = Add_mp4(url1= a.url1,url2=a.url2)
            b.hebing()
