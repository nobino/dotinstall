# Hash Object

sales = {"tanaka"=>100, "yamada"=>150, "nagata"=>300}

p sales

p sales["tanaka"]

# methods of hash object
p sales.size
p sales.length

p sales.empty?

p sales.has_key?("tanaka")
p sales.has_key?("not exists")

p sales.has_value?(100)
p sales.has_value?(10000)
