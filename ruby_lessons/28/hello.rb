# define a method

def sing(word = "la", num)
  s = ""
  for i in 1..num do
    s += word
  end
  s += "~"
  return s
end

res = sing("hu", 10)

puts res
