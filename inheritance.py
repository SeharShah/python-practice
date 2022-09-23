class Car:
    def information(self):
        print("hello i am car" )
class toyota(Car):
    def car(self):
        self.information()
    print("this is toyota car")
class corolla (Car):
    def details(self):
        self.information()
    print("this is corollla design")

object = toyota()
object.information()
abc= corolla()

#abc.information()

class Animal:
 def eat(self):
  print("It eats insects.")
 def sleep(self):
     print("It sleeps in the night.")

class Bird(Animal):
 def fly(self):
    print("It flies in the sky.")

 def sing(self):
  print("It sings a song.")
  print(issubclass(Bird, Animal))

Koyal= Bird()
print(isinstance(Koyal, Bird))

Koyal.eat()
Koyal.sleep()
Koyal.fly()
Koyal.sing()

