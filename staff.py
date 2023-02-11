# -*- coding: utf-8 -*-

import sqlite3

class Staff:
    def __init__(self):
        self.conn = sqlite3.connect('books.db')
        self.c = self.conn.cursor()
        self.chonn = sqlite3.connect('stafflogin.db')
        self.ch = self.chonn.cursor()
        
    
    def login(self):
        while True:
            staff_id = input("Enter your staff_id: ")
            staff_access_code = input("Enter your code: ")
            self.ch.execute("SELECT * FROM stafflogin WHERE staff_access_code = ? AND staff_id = ? ", (staff_access_code, staff_id))
            result = self.ch.fetchone()
            if result:
                print("Welcome, {}".format(result[1]))
                return
            else:
                print("Invalid code. Please try again.")



    def onStart(self):
        self.login()
        while True:
            print("===============================")
            print(" Library Management System ")
            print("-------------------------------")
            print("Select an option:")
            print("1. Search Books")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. Get Book")
            print("q. Quit")
            user_input = input("Enter your choice: ")
            if user_input == "1":
                self.search_books()
            elif user_input == "2":
                self.borrow_book()
            elif user_input == "3":
                self.return_book()
            elif user_input == "4":
                self.get_book()
            elif user_input == "q":
                print("Bye..")
                break
            else:
                print("Invalid input. Please try again.")

    def search_books(self):
        print("Enter search term: ")
        search_term = input()
        search_term = '%'+search_term+'%'
        self.c.execute('SELECT * FROM books WHERE title LIKE ? OR authors LIKE ?', (search_term,search_term))
        result = self.c.fetchall()
        if not result:
            print("No matching books found.")
        else:
            for book in result:
                print("ISBN: ", book[0], "Title: ", book[1], "Author: ", book[2], "Availability: ", book[3])

        
    def return_book(self):
        print("Enter ISBN: ")
        isbn = input()
        self.c.execute("UPDATE books SET available = 1 WHERE isbn = ?", (isbn,))
        self.conn.commit()
        
    def borrow_book(self):
        print("Enter ISBN: ")
        isbn = input()
        self.c.execute("UPDATE books SET available = 0 WHERE isbn = ?", (isbn,))
        self.conn.commit()
    
    def get_book(self):
        bookID = input("Enter book ID: ")
        self.cursor.execute("SELECT * FROM books WHERE bookID = :bookID", {'bookID': bookID})
        book = self.cursor.fetchone()
        if not book:
            print(f"Book with ID {bookID} is not available.")
            return
        print(f"Book details: {book}")

if __name__ == '__main__':
    staff = Staff()
    staff.onStart()