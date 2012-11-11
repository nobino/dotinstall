# array object

names = ["taro", "jiro", "hanako"]

p names

p names[0]

p names[1]

p names[1..2]

p names[0...2] # exclude 2

p names[-1] # access [length - 1]

names[0] = "taro_new"

p names[0]

names[1..2] = ["jiro_new", "hanako_new"]

p names

names[1, 2] = ["a", "b"]

p names

names [1, 0] = ["c", "d"] # insertion

p names
