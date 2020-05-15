import easygui as t
#初始置换（IP）
IP_Table = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7]
#逆初始置换IP^-1
R_IP_Table = [40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25]
#扩展变换E
E_Table = [32,  1,  2,  3,  4,  5,
            4,  5,  6,  7,  8,  9,
            8,  9,  10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1]
#S盒中的S1盒
S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
#S盒中的S2盒
S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
#S盒中的S3盒
S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
#S盒中的S4盒
S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
#S盒中的S5盒
S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
#S盒中的S6盒
S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
#S盒中的S7盒
S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
#S盒中的S8盒
S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
#S盒
S_Box = [S1, S2, S3, S4, S5, S6, S7, S8]

#置换运算P
P_table = [16,  7, 20, 21, 29, 12, 28, 17,
           1,  15, 23, 26, 5,  18, 31, 10,
           2,   8, 24, 14, 32, 27,  3,  9,
           19, 13, 30,  6, 22, 11,  4, 25]
#秘钥置换PC_1
PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
#秘钥置换PC_2
PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]
#对左移位的规定
move_times = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


def string_to_bit_array(text):  #字符串转二进制比特流
    array = list()
    for char in text:
        binval = binvalue(char, 8)  #一个字节8位转换为二进制
        array.extend([int(x) for x in list(binval)])  #转换后的二进制存入列表开头
    return array


def bit_array_to_string(array):  #二进制比特流转字符串
    res = ''.join([chr(int(y, 2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in nsplit(array, 8)]])
                #chr(ASCII值转ASCII字符)
    return res


def binvalue(val, bitsize):  #字符串形式转换为二进制值
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]    #ord(ASCII字符转ASCII数字)
    if len(binval) > bitsize:
        raise("输入长度超出限制！")
    while len(binval) < bitsize:
        binval = "0" + binval  #长度不够前面补0
    return binval


def nsplit(s, n):  #按长度n分割列表
    return [s[k:k + n] for k in range(0, len(s), n)]


ENCRYPT = 1     #加密
DECRYPT = 0     #解密


class des():
    def __init__(self):
        self.password = None            #输入秘钥
        self.text = None                #输入明文
        self.keys = list()              #生成每轮秘钥

    def run(self, key, text, action=ENCRYPT, padding=False):
        if len(key) < 8:
            raise("秘钥应该为8位字节。")
        elif len(key) > 8:
            key = key[:8]  #如果秘钥长度超过8位，截取前8位
        self.password = key
        self.text = text

        if padding and action == ENCRYPT:
            self.addPadding()
        elif len(self.text) % 8 != 0:#如果不填充，则指定的数据大小必须是8字节的倍数
            raise("数据大小应为8的倍数")
        self.generatekeys()  #生成所有密钥
        text_blocks = nsplit(self.text, 8)  #将文本分成8个字节的块，因此为64位
        result = list()
        for block in text_blocks:  #遍历所有字节块
            block = string_to_bit_array(block)  #字节块转换为二进制比特流
            block = self.permut(block, IP_Table)  #初始置换
            g, d = nsplit(block, 32)  # g(左32位), d(右32位)
            tmp = None
            for i in range(16):  #16轮循环
                d_e = self.expand(d, E_Table)  #展开d以匹配Ki大小（48位）
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], d_e)  #如果加密使用Ki与展开结果异或运算
                else:
                    tmp = self.xor(self.keys[15 - i], d_e)  #如果解密从最后一个密钥开始与展开结果异或运算
                tmp = self.substitute(tmp)  #应用S_BOX的方法
                tmp = self.permut(tmp, P_table)     #使用P置换
                tmp = self.xor(g, tmp)      #左32位于运算后的d进行异或运算
                g = d
                d = tmp
            result += self.permut(d + g, R_IP_Table)  #执行最后一个逆初始置换并将结果附加到result后
        final_res = bit_array_to_string(result)
        if padding and action == DECRYPT:
            return self.removePadding(final_res)  #解密且填充时，则移除填充
        else:
            return final_res  #返回最终加密/解密结果

    def substitute(self, d_e):  #S_BOX替换
        subblocks = nsplit(d_e, 6)  #列表按6位拆分
        result = list()
        for i in range(len(subblocks)):  #遍历所有
            block = subblocks[i]
            row = int(str(block[0]) + str(block[5]), 2)  #得到每行的第一位与最后一位
            column = int(''.join([str(x) for x in block[1:][:-1]]), 2)  #列为第2、3、4、5位
            val = S_Box[i][row][column]  #取第（i）轮所用的S_Box中的值
            bin = binvalue(val, 4)  #值转换为二进制
            result += [int(x) for x in bin]  #结果添加到末尾
        return result

    def permut(self, block, table):  #置换（泛型方法）
        return [block[x - 1] for x in table]

    def expand(self, block, table):  #置换（与permut作用相同，用于区分E_Table与其他表）
        return [block[x - 1] for x in table]

    def xor(self, t1, t2):  #应用异或并返回结果列表
        return [x ^ y for x, y in zip(t1, t2)]

    def generatekeys(self):  #生成所有密钥
        self.keys = []
        key = string_to_bit_array(self.password)
        key = self.permut(key, PC_1)  #初始置换
        g, d = nsplit(key, 28)  #分成（g->左28位），（d->右28位）
        for i in range(16):  #使用16轮循环
            g, d = self.shift(g, d, move_times[i])  #应用与回合相关的移位（不总是1）
            tmp = g + d  #合并它们 Merge them
            self.keys.append(self.permut(tmp, PC_2))  #用PC_2置换获得Ki

    def shift(self, g, d, n):  #移动列表
        return g[n:] + g[:n], d[n:] + d[:n]

    def addPadding(self):  #使用PKCS5规范向数据添加填充    假设数据3位填充5个0x05，数据1位填充7个0x07
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)

    def removePadding(self, data):  #移除纯文本的填充（假定有填充）
        pad_len = ord(data[-1])
        return data[:-pad_len]

    def encrypt(self, key, text, padding=False):
        return self.run(key, text, ENCRYPT, padding)

    def decrypt(self, key, text, padding=False):
        return self.run(key, text, DECRYPT, padding)


def main():
    while True:
        tuple = ('加密','解密','退出')
        choice = t.buttonbox('请选择以下功能','DES加解密',tuple)
        if choice == '加密':
            attention = '注：秘钥长度为8位，如果超出只截取前8位\n  明文为8位或8的倍数位'
            input_message = ['输入秘钥:', '输入明文']
            s = t.multenterbox(attention, 'DES加密', input_message)
            if s == None :
                continue
            while s[0] == '' or s[1] == '' :
                s = t.multenterbox('        请不要输入空内容！\n\n' + attention, 'DES加密', input_message)
                if s == None:
                    break
            if s == None :
                continue
            key = s[0]
            text = s[1]
            d = des()
            r = d.encrypt(key, text)
            t.msgbox('DES加密结果：' + r ,'加密结果:', '返回')
        elif choice == '解密':
            attention = '注：秘钥长度为8位，如果超出只截取前8位'
            input_message = ['输入秘钥:', '输入密文']
            s = t.multenterbox(attention, 'DES解密', input_message)
            if s == None :
                continue
            while s[0] == '' or s[1] == '' :
                s = t.multenterbox('        请不要输入空内容！\n\n' + attention, 'DES解密', input_message)
                if s == None:
                    break
            if s == None :
                continue
            key = s[0]
            text = s[1]
            d = des()
            r = d.decrypt(key , text)
            t.msgbox('DES解密结果：' + r, '解密结果:', '返回')
        else :
            return
if __name__ == '__main__':
    main()
