class A:
    def __init__(self):
        self.x = 10


class B(A):
    def __init__(self):
        super().__init__()
        self.y = self.x + 5


print(B().y)

b = B()
print(b.y)


class BasePage:
    def __init__(self, base_url):
        self.base_url = base_url

    def visit(self):
        return 'Выполнен вход по урлу ' + self.base_url


class HomePage(BasePage):
    def __init__(self, base_url):
        super().__init__(base_url)


url = HomePage('https://example.com')
print(url.visit())
