# coding: UTF-8
# formatted print

a = 10
b = 'a'
c = {'aaa':100, 'bbb':200}

print 'my age is %05d' % a  # 5桁分０で埋める

print 'my name is %s' % b

print '%s is %d years old' % (b, a)

print "print the value specified by it\'s key: %(aaa)d" % c
