# Example of multilevel inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is Eating!')

    def sleep(self):
        print (f'{self.name} is sleeping!')

class Prey(Animal):
    def flee(self):
        print( 'it can flee')

class Predator(Animal):
    def hunt(self):
        print('It will Hunt !')


class Rabit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

print()
fish = Fish('Aqua')
fish.hunt()
fish.flee()
fish.sleep()
fish.eat()
