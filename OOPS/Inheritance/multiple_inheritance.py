# Example of multiple inheritance

class Prey:
    def flee(self):
        print( 'it can flee')

class Predator:
    def hunt(self):
        print('It will Hunt !')


class Rabit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rab = Rabit()
rab.flee()

hawk = Hawk()
hawk.hunt()

print()
fish = Fish()
fish.hunt()
fish.flee()
