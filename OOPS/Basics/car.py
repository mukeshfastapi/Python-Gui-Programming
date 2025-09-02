class Car:

    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def start(self):
        print (f'Starting the {self.name}')

    def stop(self):
        print (f'Please stop {self.name} right now !!')