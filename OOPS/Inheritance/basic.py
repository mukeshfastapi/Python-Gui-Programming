# Introduction to Inheritance

class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print (f'{self.name} is sleeping')

class Dog(Animal):

    def speak(self):
        print(f'{self.name} is speaking woow')

class Cat(Animal):
    def speak(self):
        print(f'{self.name} is speaking Meow')


dog = Dog('sparrow')
dog.speak()
dog.eat()
dog.sleep()
print()
cat = Cat('Garfield')
cat.speak()
cat.eat()
cat.sleep()

