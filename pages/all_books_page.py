from bs4 import BeautifulSoup
from parser.book_parser import BookParser

from locators.all_books_page import AllBooksPageLocators

class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content,'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]
        