class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.__isbn = isbn ##Private
        self.available = available

    def display_info(self):
        print('Title =', self.title)
        print('Author =', self.author)
        print('ISBN =', self.__isbn)
        print('Available? =', self.available)

    def reveal_isbn(self): ##Getter
        print ('ISBN is',self.__isbn)

    def modify_isbn(self, new_isbn): ##Setter
        self.__isbn = new_isbn
        print(self.title+"'s ISBN is now", self.__isbn)
