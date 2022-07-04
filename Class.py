class Person:
    def __init__(self, name):
        self.name = name

    def gruss(self):
        print(f'Hallo! Ich bin {self.name}.')

    def set_name(self, neuer_name):
        self.name = neuer_name

max = Person('Tobi')
max.gruss()
max.set_name('Minann')
max.gruss()

print(max.name)

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

human = Celsius(37)

#human.temperature = 37



print(int(human.to_fahrenheit()))




