# each

users = ["taro", "jiro", "hanako"]
scores = {"taro"=>200, "jiro"=>300, "hanako"=>120}

scores.each do |name, score|
  printf("%s's score is %d\n", name, score)
end
