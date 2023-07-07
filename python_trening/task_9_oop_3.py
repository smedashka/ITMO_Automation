class Soda:
    def __init__(self, topping=None):
        self.topping = topping

    def show_my_drink(self):
        if self.topping:
            print('Газировка {}'.format(self.topping))
        else:
            print('Обычная газировка')


drink1 = Soda('Лимон')
drink1.show_my_drink()


drink2 = Soda()
drink2.show_my_drink()


