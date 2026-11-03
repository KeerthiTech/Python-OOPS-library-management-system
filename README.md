# Python OOP Library Management System

A simple program that demonstrates Object-Oriented Programming in Python.

## OOP Concepts Used

| Concept | Where it is used |
|---|---|
| Class and Objects | `Book`, `Member`, `Library` |
| Encapsulation | `Book` keeps `__is_issued` private; it changes only through `issue()` and `return_book()` |
| Abstraction | `Member` is an abstract class that forces every member type to define `max_books()` |
| Inheritance | `Student` and `Teacher` inherit from `Member` |
| Polymorphism | `max_books()` gives 2 for `Student` and 5 for `Teacher` |

## How to Run

    python library.py

## Sample Output

    'Python Basics' issued to Asha
    'Data Structures' issued to Asha
    Asha reached the limit of 2 books
    'OOP Concepts' issued to Dr. Ravi