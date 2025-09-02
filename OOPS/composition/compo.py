# Introduction to Compostion -----> Is a relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = Wheel(size)

    def display_car(self):
        return f'{self.make} {self.model} {self.engine.horse_power} {self.wheels.size}'


car1 = Car('Ford', 'Mustang', 600, 4)
car2 = Car('Lembroghini', 'Hurracane', 1200, 4)

print(car1.display_car())

