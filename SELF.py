# -*- coding: utf-8 -*-
'''class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()'''
#t代替原来的self位置
'''
class A(object):
    def __init__(self):
	    self.name='lbc'
	    print("1")
    def fun_main(self):
	    print('this is main fun')


a=A()
a.fun_main()
print(a.name)'''
#调用class A时候，会首先调用__init__

'''a='分隔'
b=raw_input(a).split()
print(b)#a没用 不会影响b的值，只用来给出输出a'''

'''upath2 = ['aaa','bbb']
upath2 = {x[0]:x[1] for x in upath2}
print upath2
'''
#result: {'a':'a','b':'b'}
#原本是一个列表，将每个元素的第一个字符作为字典key，第二个字符作为value
