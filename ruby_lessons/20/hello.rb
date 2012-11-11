# if

score = 65

if score >= 80
  puts "great!"
elsif score >= 60
  puts "so so..."
else
  puts "not so great"
end

score = 85

puts "great!" if score >= 80

# condition opreator
a = 50
b = 20

max = a > b ? a : b
p max
