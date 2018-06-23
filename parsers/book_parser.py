import re
from locators.book_locators import Book_locators


class BookParser():
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name} Price {self.price_locator} Rating {self.rating}>'

    @property
    def name(self):
        locator = Book_locators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = Book_locators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link 

    @property
    def price_locator(self):
        locator = Book_locators.PRICE_LOCATOR
        item_link = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern,item_link)
        return float(matcher.group(1))

    @property
    def rating(self):
        RATING = {
            'One' : 1,
            'Two' : 2,
            'Three' : 3,
            'Four' : 4,
            'Five' : 5
        }
        locator = Book_locators.RATING_LOCATOR
        starrating_tags = self.parent.select_one(locator).attrs['class']
        rating_class = [r for r in starrating_tags if r != 'star-rating']
        return RATING.get(rating_class[0])
        
    




        
        
        