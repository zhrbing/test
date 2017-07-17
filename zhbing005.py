# -*- coding:utf-8 -*-
# __author__ = 'zhbing'

#內建模块--datetime
# from datetime import datetime,timedelta,timezone    #导入datetime模块的类
# now=datetime.now()        #获取当前datetime
# print(now,'\t',type(now))

# dt=datetime(2017,7,14,14,32)  #用指定日期时间创建datetime
# print(dt)
# print(datetime.now().timestamp())  #把datetime转换为timestamp，小数位表示毫秒数

# t=1429417200.0
# print(datetime.fromtimestamp(t))    #timestamp转换为datetime,本地时间
# print(datetime.utcfromtimestamp(t)) #UTC标准时区时间

#str转换为datetime
# str='2015-6-1 18:19:59'
# cday=datetime.strptime(str,'%Y-%m-%d %H:%M:%S')
# print(cday,type(cday))

#datetime转换为str
# now=datetime.now()
# str1='%a,%b %d %H:%M'
# str2='%Y-%m-%d %H:%M:%S'
# print(now.strftime(str1))
# print(now.strftime(str2))

#datetime加减
# now=datetime.now()
# print(now)
# print(now+timedelta(hours=3))
# print(now-timedelta(days=2))
# print(now+timedelta(days=2,hours=3))

# tz_utc8=timezone(timedelta(hours=8))    #创建时区UTC+8:00
# now=datetime.now()
# print(now)
# dt=now.replace(tzinfo=tz_utc8)  #强制设置为UTC+8:00
# print(dt)
#如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区

# utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
# print('UTC时间：',utc_dt)   # 拿到UTC时间，并强制设置时区为UTC+0:00
#
# bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
# print('北京时间：',bj_dt)    # astimezone()将转换时区为北京时间
#
# tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
# print('东京时间：',tokyo_dt) # astimezone()将转换时区为东京时间
#
# tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
# print('东京时间：',tokyo_dt2)    # astimezone()将转换时区为东京时间

################################################################################
#內建模块collections
#namedtuple
# from collections import namedtuple
# Point=namedtuple('Point',['x','y']) # namedtuple('名称', [属性list])
# p=Point(1,2)
# print(p.x,p.y)
# print(isinstance(p,Point),isinstance(p,tuple))

#deque:高效实现插入和删除操作的双向列表，适合用于队列和栈
# from collections import deque
# q=deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q)
# q.popleft()
# print(q)
# q.pop()
# print(q)

#计数器Counter
# from collections import Counter
# cnt=Counter()
# for ch in 'programming developing':
#     cnt[ch]+=1
#
# print(cnt)
################################################################################
#hashlib
import hashlib

#md5生成结果是128bit，通常用32位16进制字符串表示
md5=hashlib.md5()

# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# md5.update('123456'.encode('utf-8'))
# print(md5.hexdigest())

#分块多次调用，计算结果一样
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())

#sha1生成结果是160bit，通常用40位16进制字符串表示
# sha1=hashlib.sha1()
# sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())
################################################################################









