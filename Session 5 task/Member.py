class Member:
    def __init__(self, name, id, books=None):
        self.name = name
        self.__id = id ##Private
        self.books = []

    def borrow_book(self, book):
        if book in self.books:
            print(self.name,'already has', book.title)
            return
        elif not book.available:
            print(book.title,'is not available for borrowing')
            return
        else:
            self.books.append(book)
            book.available = False
            print(self.name, 'has borrowed ', book.title)
            return

    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)
            book.available = True
            print(self.name, 'has returned ', book.title)
            return
        else:
            print(self.name, 'does not have ', book.title, 'to return')
            return
        
    def reveal_id(self): ##Getter
        print('Member ID is',self.__id)

    def modify_id(self, new_id): ##Setter
        self.__id = new_id
        print(self.name+"'s ID is now", self.__id)