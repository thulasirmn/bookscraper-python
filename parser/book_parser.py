import re
from locators.book_locators import Book_locators


class BookParser():
    def __init__(self, parent):
        self.parent = parent

    @property
    def name(self):
        locator = Book_locators.NAME_LOCATOR
        item_link = self.parent.selectone(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = Book_locators.LINK_LOCATOR
        item_link = self.parent.selectone(locator).attrs['href']
        return item_link 

    @property
    def price_locator(self):
        locator = Book_locators.PRICE_LOCATOR
        item_link = self.parent.selectone(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern,item_link)
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = Book_locators.RATING_LOCATOR
        starrating_tags = self.parent.selectone(locator).attrs['class']
        rating_class = [r for r in starrating_tags if r != 'star-rating']
        
    




        
        
        