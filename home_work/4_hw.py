class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


rectangle1 = Rectangle(5, 8)
print(rectangle1.calculate_area())
print(rectangle1.calculate_perimeter())

rectangle2 = Rectangle(2, 9)
print(rectangle2.calculate_area())
print(rectangle2.calculate_perimeter())

rectangle3 = Rectangle(7, 4)
print(rectangle3.calculate_area())
print(rectangle3.calculate_perimeter())


print('---------------')


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


elem = Math(20, 4)
print(elem.addition())
print(elem.multiplication())
print(elem.division())
print(elem.subtraction())


print('---------------')


class Button:
    type: str = 'Кнопка'

    def __init__(self, text, loc=''):
        self.text = text
        self.loc = loc

    def click(self):
        return "Клик по кнопке {}".format(self.text)


text_box = Button('Text Box')
check_box = Button('Check Box')
radio_button = Button('Radio Button')
web_tables = Button('Web Tables')
buttons = Button('Buttons')
links = Button('Links')
broken_links_images = Button('Broken Links - Images')
upload_download = Button('Upload and Download')
dynamic_properties = Button('Dynamic Properties')

print(text_box.text)
print(text_box.click() + '\n')

print(check_box.text)
print(check_box.click() + '\n')

print(radio_button.text)
print(radio_button.click() + '\n')

print(web_tables.text)
print(web_tables.click() + '\n')

print(buttons.text)
print(buttons.click() + '\n')

print(links.text)
print(links.click() + '\n')

print(broken_links_images.text)
print(broken_links_images.click() + '\n')

print(upload_download.text)
print(upload_download.click() + '\n')

print(dynamic_properties.text)
print(dynamic_properties.click() + '\n')

