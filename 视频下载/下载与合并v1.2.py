import requests
import threading
from tkinter import * 
import os


'''需要自己更改的变量'''
url = 'https://······/000000.ts'
begin = 0  # 视频流(.ts)开始号
end = 3  # 视频流(.ts)结束号
long = 3  # 视频流号码变化长度 例如：下载00000.ts到11111.ts时，长度为5
path = 'F:\\'  # 保存视频流（.ts）的路径
name = 'movie.mp4'  #默认合成文件名

'''全局变量'''
lock = threading.Lock()  # 只是定义一个锁
threads = []  # 多线程存放进程


class Downalod_and_Add():
    def __init__(self, url, begin, end, long, path):
        self.url = url
        self.begin = begin
        self.end = end
        self.long = long
        self.path = path
        self.download_num = 0  # 已下载视频流数量
        self.undownloads = []  # 没有下载列表

    def thread_download_mp4(self):  # 多线程下载视频流
        for i in range(self.begin, self.end):
            self.url, i = self.get_url(self.url, self.long, i)
            t = threading.Thread(target=self.download_mp4, args=(self.url, i))  # 添加线程到线程列表
            threads.append(t)
            t.start()  # 启动线程
        for t in threads:
            t.join()
    def get_url(self, url, long, i):  # 按照规定生成url
        temp = url[::-1].split('.', 1)
        url = temp[1][::-1]
        type = '.' + temp[0][::-1]
        i = str(i).zfill(long)  # 补全长度 long为4时，1补全为0001
        url = url[:-long] + str(i) + type
        return url, i
    def download_mp4(self, url, i):  # 下载单个视频流
        name = str(i) + '.mp4'
        try:
            flag = 0
            f = open(self.path + name, 'rb')
            f.read()
            f.close()
            self.download_num += 1
        except:
            flag = 1
        if flag:
            print('正在下载：' + name)
            self.undownloads.append(name)
            response = requests.get(url)
            if response.status_code == 200:
                f = open(self.path + name, 'wb')
                f.write(response.content)
                f.close()
                self.undownloads.remove(name)
                os.system('cls')
                self.download_num += 1
                print('正在下载列表：')
                for undownload in self.undownloads:
                    print(undownload, end='\t')
                print(
                    '\n------------------------------------------------------------------------------------------------------------------------'
                    '\n\n' + name + '下载完成\t还有' + str(self.end - self.download_num - self.begin) + '个没有下载完成')
                self.show_percnet(self.download_num, self.end - self.begin)
            else:
                return
    def show_percnet(self, num, total):  # 显示已下载百分比
        percent = num / total * 100
        rank = int(percent) / 10
        str = '<'
        for i in range(1, 21):
            if i / 2 < rank:
                str += '■'
            else:
                str += '-'
        str += '>已下载%.2f%s'
        print(str % (percent, '%'))

    def add_mp4(self,file_name):  # 合并视频流文件
        for i in range(self.begin, self.end):
            i = str(i).zfill(long)
            name = str(i) + '.mp4'
            try:
                f = open(self.path + name, 'rb')
                data = f.read()
                p = open(file_name, 'ab')
                p.write(data)
                f.close()
                p.close()
            except:
                pass

class Panel():  # 可视化界面
    def __init__(self):
        self.master = Tk()
        self.url = StringVar()
        self.begin = StringVar()
        self.end = StringVar()
        self.long = StringVar()
        self.name = StringVar()
        self.path = StringVar()
    def default_value(self):#变量赋默认值
        self.url.set(url)
        self.begin.set(begin)
        self.end.set(end)
        self.long.set(long)
        self.name.set(name)
        self.path.set(path)
    
    def run_d(self):#下载功能
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        download = Downalod_and_Add(self.url.get(),int(self.begin.get()),int(self.end.get()) + 1,int(self.long.get()),self.path.get())
        download.thread_download_mp4()
        print('\n------------------------------------------------------------------------------------------------------------------------\n\n下载完成')
    def run_a(self):#合并功能
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        add = Downalod_and_Add(self.url.get(),int(self.begin.get()),int(self.end.get()) + 1,int(self.long.get()),self.path.get())
        add.add_mp4(self.name.get())
        print(self.name.get())
        print('\n------------------------------------------------------------------------------------------------------------------------\n\n合并完成')
    
    def main(self):#主要界面构成
        self.master.title('视频下载与合并')  # 窗口标题
        self.master.geometry('700x150')  # 窗口大小
        self.default_value()
        #标签
        l1 = Label(self.master, text='Url：', font=("Arial", 13))#标签
        l1.grid(row=0, column=0) #位置
        insert = Entry(self.master, textvariable=self.url, width=80)#输入框
        insert.grid(row=0, column=1, columnspan=8)
        l2 = Label(self.master, text='Begin：', font=("Arial", 13))
        l2.grid(row=1, column=0) 
        insert = Entry(self.master, textvariable=self.begin, width=10)
        insert.grid(row=1, column=1)
        l3 = Label(self.master, text='End：', font=("Arial", 13))
        l3.grid(row=1, column=2)  
        insert = Entry(self.master, textvariable=self.end, width=10)
        insert.grid(row=1, column=3)
        l4 = Label(self.master, text='long：', font=("Arial", 13))
        l4.grid(row=1, column=4) 
        insert = Entry(self.master, textvariable=self.long, width=10)
        insert.grid(row=1, column=5)
        l5 = Label(self.master, text='Name：', font=("Arial", 13))
        l5.grid(row=1, column=6)  
        insert = Entry(self.master, textvariable=self.name, width=10)
        insert.grid(row=1, column=7)
        l6 = Label(self.master, text='Path：', font=("Arial", 13))
        l6.grid(row=2, column=0)  
        insert = Entry(self.master, textvariable=self.path, width=80)
        insert.grid(row=2, column=1, columnspan=8)
        # 按钮
        button1 = Button(self.master, text='Download', command=self.run_d)
        button1.grid(row=3, column=2, ipadx=20, ipady=10)
        button2 = Button(self.master, text='Add', command=self.run_a)
        button2.grid(row=3, column=4, ipadx=20, ipady=10)
        # 显示可视化
        mainloop()

if __name__ == '__main__':
    main = Panel()
    main.main()

