from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self): pass


class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("\nFormatted output")
        print("Title: {}\nAuthor: {}\nPrice: {}".format(self.title, self.author, self.price))


if __name__ == '__main__':
    title = input("Enter a book title: ")
    author = input("Enter an author: ")
    price = int(input("Enter a price: "))
    new_novel = MyBook(title, author, price)
    new_novel.display()
