from time import time


def timelog(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Working time is: {round(t2-t1, 10)} sec')
        return result
    return wrapper


class Product:

    __meta = 'Analitics signal'

    def __init__(self, name):
        self.product = name

    @timelog
    def add_to_cart(self, count):
        print(f'Add {count} products [{self.product}] to cart')
        print(f'Add {count} products [{self.product}] to cart')
        print(f'Add {count} products [{self.product}] to cart')
        print(f'Add {count} products [{self.product}] to cart')
        print(f'Add {count} products [{self.product}] to cart')

    def edit_description(self):
        print(f'Edit Description')

    def add_review(self, text):
        print(f'Add review: ', text)


class Form:
    product = None

    def save_product_form(self):
        print(f'Save [{self.product}] to database')


class Book(Product, Form):

    @timelog
    def __init__(self, name, author, pages):
        super().__init__(name=name)
        self.name = name
        self.author = author
        self.pages = pages

    def __add__(self, other):
        return Book(
            name=f'{self.name}|{other.name}',
            author=f'{self.author}|{other.author}',
            pages=self.pages + other.pages,
        )

    def __str__(self):
        return f'Book: {self.author} : "{self.name}"'

    def get_pages_count(self):
        print(f'pages count in this book: {self.pages}')

    @timelog
    def add_to_cart(self, count):
        super().add_to_cart(count)
        print(f'{count} products [{self.product}] added to cart')
