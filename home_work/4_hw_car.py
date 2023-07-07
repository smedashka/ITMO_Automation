class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def stop(self):
        print('Автомобиль заглушен')

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.year = type

    def set_color(self, color):
        self.color = color


car = Car("black", "crossover", 2005)
car.start()
car.stop()
print('Цвет {}, тип {}, год {}'.format(car.color, car.type, car.year))
car.set_year(2010)
print('Цвет {}, тип {}, год {}'.format(car.color, car.type, car.year))
