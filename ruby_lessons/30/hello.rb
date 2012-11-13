# Class

class Monster # start with upper-case
  def initialize # constructor in Java
    @name = name
    @hp = 100 + rand(100)
  end

  def damege
    @hp -= 10 + rand(10)
    printf("%s's hp is now %d\n", @name, @hp)
  end
end
