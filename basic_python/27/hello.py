# coding: utf-8
# map function, 無名関数

def double(x):
    return x * x

print map(double, [1, 3, 5])
print map(lambda x:x * x, [2, 4, 6])
