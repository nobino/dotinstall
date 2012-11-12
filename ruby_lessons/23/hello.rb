# case

signal = "yellow"

case signal
when "red"
  puts "stop!"
when "green", "blue"
  puts "go!"
when "yellow"
  puts "caution!"
else
  puts "signal is broken"
end
