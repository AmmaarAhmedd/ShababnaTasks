from Book import Book
from Member import Member
from StaffMember import StaffMember

book1 = Book('1984', 'George Orwell', '1234567890')
book2 = Book('To Kill a Mockingbird', 'Harper Lee', '0987654321')
book3 = Book('The Great Gatsby', 'F. Scott Fitzgerald', '1122334455', available=False)
member1 = Member('Alice', 'M001', [])
member2 = Member('Bob', 'M002', [])

book2.display_info()
member1.borrow_book(book2)
print (member1.books[0].title)
print (book2.available)
member1.return_book(book2)
print (book2.available)

staffmember1 = StaffMember('Carol', 'M003', 'S001', [])
print(book3.available)
staffmember1.add_book(book3)
print(book3.available)


member1.borrow_book(book1)
member1.borrow_book(book2)
member1.borrow_book(book3)
book = 0
for book in member1.books:
    print(book.title)
    book =+ 1

book1.reveal_isbn()
member1.reveal_id()

book1.modify_isbn('ii123987')
member1.modify_id('K0978')