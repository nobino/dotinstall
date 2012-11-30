# coding: UTF-8
# 10 list-1

a = [1, 2, 'a', 5.5]
b = list([3, 5])

print a
print b

# len, +, *, [], [start:end]

print len(a)
print a + b
print a * 2
print a[2]

a[2] = 'b'
print a

a[2:4] = ['b', 'c']
print a
