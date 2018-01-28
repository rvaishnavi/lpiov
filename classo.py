class Book:
    __name = None
    __author = None
    __pages = None
    __price = None

    def __init__(self, name, author, pages, price):
        self.name = name
        self.__author = author
        self.__pages = pages
        self.price = price + 10

    def get_pages(self):
        return self.__pages

    def new_pages(self,pages):
        self.__pages = self.__pages - pages
        return self.__pages

    def display(self):
        return "I have {} book, whose author is {}, " \
           "{} pages and a price of {}$".format(self.name,
                                               self.__author,
                                               self.__pages,
                                               self.price)


book1 = Book('myown', 'myself', 20, 52)
book2 = Book('noname', 'itsme', 200, 13)
print(book1.display())
# Prints - I have myown book, whose author is myself, 20 pages and a price of 62$

print(book2.display())
# Prints - I have noname book, whose author is itsme, 200 pages and a price of 23$

if book1.price > book2.price:
    print(book1.name, "book is costly than", book2.name)
else:
    print(book1.name, "book is cheaper than", book2.name)
# prints - myown book is costly than noname

print(book1.get_pages())  # 20

tornpages = 2
print(book1.new_pages(tornpages))  # 18
print(book1.get_pages())  # 18


class Fiction(Book):
    __rating = None

    def __init__(self, name, author, pages, price, rating):
        self.__rating = rating

        super(Fiction,self).__init__(name, author, pages, price)

    def get_rating(self):
        return self.__rating


book3 = Fiction('ficbook', 'againme', 466, 150, 4)

print(book3.get_pages(), book3.get_rating())  # 466 4