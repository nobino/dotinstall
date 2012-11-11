# date and time

t1 = Time.now

p t1
p t1.year
p t1.month

t2 = Time.mktime(2012, 11, 11, 11, 11)
p t2

p t1 + 10 # add seconds

p t2.strftime("%Y/%m/%d")
