import requests
from locators.all_books_page import AllBooksPageLocators
from pages.all_books_page import AllBooksPage

book_content = requests.get('http://books.toscrape.com/').content
book_tag = AllBooksPage(book_content)

for book in book_tag.books:
    print (book)