# coding: utf-8
# function
# param
#  - named
# return

def hello(name, num = 1):
    return 'hello! %s. '  % name * num

s1 = hello(name='Tom')
s2 = hello(num=2, name='Steve')

print s1
print s2

def hello2():
    pass

hello2()
