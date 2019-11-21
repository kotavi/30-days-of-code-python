from collections import defaultdict

from hackerrank.library_catalog.book import Book


class Catalog:

    current_day = 0

    def __init__(self, collection, length_of_checkout = 7, initial_fee = 0.50, fee_per_late_day = 1.00):
        self.book_collection = collection
        self.length_of_checkout = length_of_checkout
        self.initial_fee = initial_fee
        self.fee_per_late_day = fee_per_late_day

    def get_current_day(self):
        return self.current_day

    def get_book_collection(self):
        return self.book_collection

    def get_book(self, book_title):
        return self.get_book_collection().get(book_title)

    def get_length_of_checkout(self):
        return self.length_of_checkout

    def get_initial_fee(self):
        return self.initial_fee

    def get_fee_per_late_day(self):
        return self.fee_per_late_day

    def set_next_day(self):
        self.current_day += 1

    def set_day(self, day):
        self.current_day = day

    def check_out_book(self, book_title):
        book = self.get_book(book_title)
        if book.get_is_checked_out():
            self.sorry_book_checked_out(book_title)
        else:
            book.set_is_checked_out(True, self.current_day)
            print("You just checked out {}. It is due on day {}."
                  .format(book_title, self.get_current_day() + self.get_length_of_checkout()))

    def return_book(self, book_title):
        book = self.get_book(book_title)
        days_late = self.current_day - (book.get_day_checked_out() + self.get_length_of_checkout())
        if days_late > 0:
            print("You owe the library ${} because your book is {} days overdue"
                  .format(self.get_initial_fee()  + days_late * self.get_fee_per_late_day(), days_late))
        else:
            print("Book is returned. Thank you.")
        book.set_is_checked_out(False, -1)

    def sorry_book_checked_out(self, book_title):
        book = self.get_book(book_title)
        print("Sorry, {} is already checked out. It should be back on day {}."
              .format(book.title, book.get_day_checked_out() + self.get_length_of_checkout()))


if __name__ == '__main__':
    book_collections = defaultdict()
    harry = Book("Harry Potter", 1999, 37843645)
    print(harry)
    book_collections["Harry Potter"] = harry
    catalog = Catalog(book_collections)
    catalog.check_out_book("Harry Potter")
    catalog.set_next_day()
    catalog.check_out_book("Harry Potter")
    catalog.set_day(17)
    catalog.return_book("Harry Potter")
    catalog.check_out_book("Harry Potter")
    print(harry)
    catalog.set_next_day()
    catalog.set_next_day()
    catalog.set_next_day()
    catalog.return_book("Harry Potter")
