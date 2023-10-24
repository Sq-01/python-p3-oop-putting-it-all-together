#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

# Tests
if __name__ == "__main__":
    book = Book("And Then There Were None", 272)
    assert book.page_count == 272
    assert book.title == "And Then There Were None"

    captured_out = io.StringIO()
    sys.stdout = captured_out
    book.page_count = "not an integer"
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "page_count must be an integer\n"

    book = Book("The World According to Garp", 69)
    captured_out = io.StringIO()
    sys.stdout = captured_out
    book.turn_page()
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "Flipping the page...wow, you read fast!\n"
    
        