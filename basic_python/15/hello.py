# coding: UTF-8
# 辞書型
# 順番は保証されない

a = {"aaa":200, "bbb":300, "ccc":500}

print a
print a["aaa"]

a["bbb"] = 5000
print a

# in
print "aaa" in a
print "xxx" in a

print a.keys()
print a.values()
print a.items()  # return a list of tupples
