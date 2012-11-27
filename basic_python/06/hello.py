# coding: UTF-8
# String
# " '
# escape \n \t \\

print 'hello'

print 'it\'s a pen.'

print '\\n\n\\t\ttab'

print '''<html>
  <head></head>
  <body style="color: red;">
  </body>
</html>
'''

print u'こんにちわ。'

# String Operation
# cat
print 'hello' + 'world'

# rep
print u'La' * 10

# length
print len('abcde')

# substring
s = 'abcdefghi'
print s[1]
print s[1:5] # exclude 5
print s[:5]
print s[3:]
print s[1:-1] # マイナスの値は-1スタートで右から数える。

# search
print s.find('cd')
print s.find('xxx') # not found return -1

# search and substring
print s[s.find('ef'):s.find('ef') + 3]
