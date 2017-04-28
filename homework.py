# -*- coding: UTF-8 -*-
import re
import jieba
class ChinneseMatching():# 封装成一个类
    def __init__(self, string, times):
        self.string = string
        self.times = times
        def writein (self):# 读入函数
            s1 = self.string.decode('utf-8') #将输入的关键字编码为unicode
            f = open('/home/pengqin/ 桌面 /1.txt', 'r')# 打开桌面的文件，读入
            for line in f.readlines():
                k = line.decode('utf-8')#对文件的每一行进行编码成unicode
                self.times = 0# 计算次数
                match = re.search(self.string.decode('utf-8'),k )
                if match == self.string.decode('utf-8')
                    self.times = self.times + 1# 如果匹配成功，那么次数加1
            f.close()# 读取完后，关闭文件
            print'The time of emerging is',self.times# 输出关键词出现次数


x = input("The key word is ")#输入关键词
dt =  ChinneseMatching(x,0)#实例化
dt.writein()#运行函数








