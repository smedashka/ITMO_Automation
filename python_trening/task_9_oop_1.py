from python_trening.task_9_checks import Checks


class Input(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


search = Input('input#search', 'Поиск')
# print(search.loc + ' ' + search.text)
print(search.check_text())


class Button(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


button = Button('button', 'Кнопка')
# print(button.loc + ' ' + button.text)
print(button.check_text())


class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


title = Title('title', 'Заголовок')
# print(title.loc + ' ' + title.text)
print(title.check_text())


class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text


link = Link('link', 'Ссылка')
# print(link.loc + ' ' + link.text)
print(link.check_text())
