# Explains and Introducing duck typing

class Animal:
    alive = True


class Dog (Animal):

    def speak(self):
        return 'Woof!'


class Cat (Animal):

    def speak(self):
        return 'Meow!'

class Car:
    alive = False
    def speak(self):
        return "Hunk"


animal = [Dog (), Cat (), Car()]

for animal in animal:
    print (animal.speak ())
    print (animal.alive)
