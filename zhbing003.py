# -*- coding:utf-8 -*-
# __author__ = 'zhbing'

#错误处理
# try:
#     print('try...')
#     r=10/int(input('Input a interger:'))
#     print('result:',r)
# except ValueError as e:
#     print('Value:',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:',e)
# else:     #没有错误发生时，自动执行
#     print('No error!')
# finally:
#     print('finally...')
# print('end...')


#logging模块记录错误信息，让程序继续执行
# import logging
# def foo(s):
#     return 10/int(s)
#
# def bar(s):
#     return foo(s)*2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('end...')

#调试
# import logging
# logging.basicConfig(level=logging.INFO)
# n=0
# logging.info('n=%d' % n)
# print(10/n)

#单元测试
# class Dict(dict):          #被测试的类：行为和dict一致，但可以通过属性访问
#     def __init__(self,**kw):
#         super().__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key]=value
#
# import unittest
# class TestDict(unittest.TestCase):    #测试类：从unittest.TestCase继承
#     def test_init(self):              #以test开头的方法是测试方法，不以test开头的方法测试时不会执行
#         d=Dict(a=1,b='test')
#         self.assertEqual(d.a,1)       #断言判断
#         self.assertEqual(d.b,'test')
#         self.assertTrue(isinstance(d,dict))
#
#     def test_key(self):
#         d=Dict()
#         d['key']='value'
#         self.assertEqual(d.key,'value')
#
#     def test_attr(self):
#         d=Dict()
#         d.key='value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'],'value')
#
#     def test_keyerror(self):
#         d=Dict()
#         with self.assertRaises(KeyError):
#             value=d['empty']
#
#     def test_attrerror(self):
#         d=Dict()
#         with self.assertRaises(AttributeError):
#             value=d.empty
#
#     def setUp(self):            #setUp()和tearDown()分别在每调用一个测试方法的前后被执行
#         print('Test start<<<')
#
#     def tearDown(self):
#         print('             >>>Test end')
#
# if __name__=='__main__':
#     unittest.main()
#
# d=Dict(a=1,b='test')
# print(d['a'])
# print(d.b)
################################################
#文件读写
# with open('/home/zhbing/桌面/000','r') as f:     #与try ... finally是一样的，但代码更简洁，且不必调用f.close()方法
#     print(f.read())             #read()一次性读取文件全部内容
#     print(f.read(10))            #read(size)每次最多读取size个字节的内容
#     print(f.readline())             #readline()每次读取一行
#     print(f.readlines())            #readlines()一次性读取所有内容并按行返回list
#     for line in f.readlines():
#         print(line.strip())     #去掉末尾的\n

# with open('/home/zhbing/桌面/111','w') as f:
#     f.write('\nHello world3.\n')
################################################
#StringIO
# from io import StringIO
# f=StringIO()
# print(f.write('hello'))
# print(f.getvalue())       #getvalue()获得写入后的str

# from io import StringIO
# f=StringIO('Hello,\nHi,\nGoodbye!')    #初始化StringIO
# while True:
#     s=f.readline()
#     if s=='':
#         break
#     print(s.strip())
################################################
#BytesIO
# from io import BytesIO
# f=BytesIO()
# print(f.write('中文'.encode('utf-8')))
# print(f.getvalue())

# from io import BytesIO
# f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())















