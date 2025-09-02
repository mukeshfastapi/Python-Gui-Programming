# Abstract classes

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# veh = Vehicle()

class Car(Vehicle):
    def go(self):
        print('Please Start The Car!')

    def stop(self):
        print ('Please Stop The Car!')

    def cruise(self):
        print('Speed on limitor')


class Bike(Vehicle):
    def go(self):
        print('Please Start The Car!')

    def stop(self):
        print ('Please Stop The Car!')

    def sensor(self):
        print('Sensor got ON!!!')

car1 = Car()
car1.go()
car1.stop()
car1.cruise()

print()
bike = Bike()
bike.go()
bike.stop()
bike.sensor()

