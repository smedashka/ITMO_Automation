class Button:
    def __init__(self, text, link):
        self.text = text
        self.link = link


home = Button('Главная', '/main')
catalog = Button('Каталог', '/catalog')

print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog.text)
print('Кнопка ' + catalog.text + ' имеет ссылку ' + catalog.link)


class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)


home_two = ButtonTwo('Главная', '/home', 'button#home')
print(home_two.click())


