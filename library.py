from abc import ABC, abstractmethod


# ---------- CLASS + ENCAPSULATION ----------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_issued = False        # private: cannot be changed directly

    def issue(self):
        if self.__is_issued:
            return False
        self.__is_issued = True
        return True

    def return_book(self):
        self.__is_issued = False

    def is_issued(self):
        return self.__is_issued


# ---------- ABSTRACTION ----------
class Member(ABC):
    def __init__(self, name):
        self.name = name
        self.borrowed = []

    @abstractmethod
    def max_books(self):                # every child MUST define this
        pass


# ---------- INHERITANCE + POLYMORPHISM ----------
class Student(Member):
    def max_books(self):
        return 2


class Teacher(Member):
    def max_books(self):
        return 5


# ---------- OBJECTS WORKING TOGETHER ----------
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, member, title):
        if len(member.borrowed) >= member.max_books():
            print(f"{member.name} reached the limit of {member.max_books()} books")
            return
        for book in self.books:
            if book.title == title and book.issue():
                member.borrowed.append(book)
                print(f"'{title}' issued to {member.name}")
                return
        print(f"'{title}' is not available")

    def return_book(self, member, title):
        for book in member.borrowed:
            if book.title == title:
                book.return_book()
                member.borrowed.remove(book)
                print(f"'{title}' returned by {member.name}")
                return
        print(f"{member.name} has not borrowed '{title}'")


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("Python Basics", "Guido"))
    lib.add_book(Book("Data Structures", "Knuth"))
    lib.add_book(Book("OOP Concepts", "Booch"))

    s = Student("Asha")
    t = Teacher("Dr. Ravi")

    lib.issue_book(s, "Python Basics")
    lib.issue_book(s, "Data Structures")
    lib.issue_book(s, "OOP Concepts")     # refused: student limit is 2
    lib.issue_book(t, "OOP Concepts")     # works: teacher limit is 5
    lib.return_book(s, "Python Basics")
    lib.issue_book(s, "OOP Concepts")     # refused: already issued to teacher