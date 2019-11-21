class Book:

    day_checked_out = -1

    def __init__(self, title, page_count, isbn, is_checked_out = False):
        self.title = title
        self.page_count = page_count
        self.isbn = isbn
        self.is_checked_out = is_checked_out

    def __str__(self):
        if self.is_checked_out:
            message = "The book: {}, {} pages, {} isbn (book is checked out)".format(self.title, self.page_count, self.isbn)
        else:
            message = "The book: {}, {} pages, {} isbn (book is available for check out)".format(self.title, self.page_count, self.isbn)
        return message

    def get_title(self):
        return self.title

    def get_page_count(self):
        return self.page_count

    def get_isbn(self):
        return self.isbn

    def get_is_checked_out(self):
        return self.is_checked_out

    def get_day_checked_out(self):
        return self.day_checked_out

    def set_is_checked_out(self, new_is_checked_out, current_day_checked_out):
        self.is_checked_out = new_is_checked_out
        self.set_day_checked_out(current_day_checked_out)

    def set_day_checked_out(self, day):
        self.day_checked_out = day
