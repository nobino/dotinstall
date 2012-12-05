# coding: UTF-8
# set (集合型)

a = set(['a', 'b', 'c', 'c'])  # cは１つしか登録されない
print a

b = set(['a', 'b', 'd'])

print a - b  # minus
print a | b  # union
print a & b  # and
print a ^ b  # exor
