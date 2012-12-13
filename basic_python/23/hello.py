# conding: UTF-8
# while

n = 0

while n < 10:
    if n == 3:
        print 'break'
        break
    print n
    n += 1
else:
    print 'end'

n = 0

while n < 10:
    if n == 3:
        print 'continue'
        n += 1
    print n
    n += 1
else:
    print 'end'
