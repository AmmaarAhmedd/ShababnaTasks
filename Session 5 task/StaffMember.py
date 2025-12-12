from Member import Member

class StaffMember(Member):
    def __init__(self, name, id, staff_id, books=None):
        super().__init__(name, id, books)
        self.staff_id = staff_id
        
    def add_book(self, book):
        book.available=True
        print(self.name,'added',book.title,'to the library')