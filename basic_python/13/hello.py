# coding: UTF-8
# タプル (unmodifieable)

a = (1, 5, 3)

print a

print len(a)

print a[1]

# error!
# a[0] = 10

# タプル、リストの相互変換
b = list(a)

print b
b[0] = 10 # OK

c = tuple(b)

print c

c[0] = 10 # error
