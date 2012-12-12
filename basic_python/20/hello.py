# coding: UTF-8
sum = 0
for i in [1, 3, 4, 5, 7, 11]:
    sum += i
else:
    print sum  # 終了時の処理を明示できる

for i in range(10):
    if i == 5:
        continue
    if i == 8:
        break  # elseブロックも実行されない
    print i
else:
    print 'end'

a = {'aaa':100, 'bbb':200, 'ccc':300}
for k, v in a.iteritems():
    print 'key: %s, value: %s' % (k, v)

for k in a.iterkeys():
    print 'key: %s' % (k)

for v in a.itervalues():
    print 'value: %s' % (v)
