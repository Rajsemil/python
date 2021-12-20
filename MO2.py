class Animal:
    def sound(self):
        print("Animal make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()