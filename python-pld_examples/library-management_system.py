#!/usr/bin/python3


class Book:
    def __init__(self, title, author, isbn, is_checked_out):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_checked_out = is_checked_out

    def check_out():
        pass
    def return_book():
        pass

class Library:
    def __init__(self, books):
        self.__books = books

    def add_book(book):
        pass

    def remove_book(isbn):
        pass

    def find_book_by_title(title):
        pass

    def list_avaliable_books():
        pass


class Member:
    def __init__(self, name, member_id, borrowed_books):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = borrowed_books

    def borrow_book(book):
        pass

    def return_book(book):
        pass
