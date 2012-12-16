# coding: utf-8
# Object

class Person(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print 'my name is %s' % self.name

class SuperPerson(Person):
    def shout(self):
        print "%s is SUPER!" % self.name

bob = Person('Bob')
print bob.name
bob.greet()

tom = SuperPerson('Tom')
tom.shout()
