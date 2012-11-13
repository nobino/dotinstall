# define a method

def sing(word = "la") #args with a default value
  puts word + word + word + "~"
end

sing()
sing("hu")
