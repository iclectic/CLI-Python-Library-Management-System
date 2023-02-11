import sqlite3
import datetime


class Librarian:
    def __init__(self):
        self.conn = sqlite3.connect('books.db')
        self.konn = sqlite3.connect('login.db')
        self.donn = sqlite3.connect('studentlogin.db')
        self.fonn = sqlite3.connect('stafflogin.db')
        self.jonn = sqlite3.connect('externaluserlogin.db')
        self.cursor = self.conn.cursor()
        self.kursor = self.konn.cursor()
        self.dursor = self.donn.cursor()
        self.fursor = self.fonn.cursor()
        self.jursor = self.jonn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (bookID INT PRIMARY KEY, title TEXT, authors TEXT, average_rating FLOAT, isbn INT, isbn13 INT, language_code TEXT, num_pages INT, ratings_count INT, text_reviews_count INT, publication_date DATE, publisher TEXT, Available TEXT)''')
    
    
    
    def onStart(self):
        while True:
            print("===============================")
            print(" Library Management System ")
            print("-------------------------------")
            print("Select an option:")
            print("1. remove book")
            print("2. add book")
            print("3. get all books")
            print("4. get book(s)")
            print("5. remove user(s)")
            print("6. get all users")
            print("7. add user")
            print("8. issue book")
            print("9. Calculate fine")
            print("10. add student login record(s)")
            print("11. add staff login record(s)")
            print("12. add external user login record(s)")
            print("13. remove student user login record(s)")
            print("14. remove staff login record(s)")
            print("15. remove external user login record(s)")
            print("q. Quit")
            user_input = input("Enter your choice: ")
            if user_input == "1":
                self.remove_book()
            elif user_input == "2":
                self.add_book()
            elif user_input == "3":
                self.get_all_books()
            elif user_input == "4":
                self.get_book()
            elif user_input == "5":
                self.remove_user()
            elif user_input == "6":
                self.get_all_users()
            elif user_input == "7":
                self.add_user()
            elif user_input == "8":
                self.issue_book()
            elif user_input == "9":
                self.impose_fine()
            elif user_input == "10":
                self.addto_studentlogin()
            elif user_input == "11":
                self.addto_stafflogin()
            elif user_input == "12":
                self.addto_externaluserlogin()
            elif user_input == "13":
                self.remove_stafflogindetails()
            elif user_input == "14":
                self.remove_studentlogindetails()
            elif user_input == "14":
                self.remove_externaluserdetails       
            elif user_input == "q":
                print("Bye..")
                break
            else:
                print("Invalid input. Please try again.")

    def remove_book(self):
        bookID = input("Enter book ID: ")
        self.cursor.execute("SELECT * FROM books WHERE bookID = :bookID", {'bookID': bookID})
        book = self.cursor.fetchone()
        if not book:
            print(f"Book with ID {bookID} is not available.")
            return
        with self.conn:
            self.cursor.execute("DELETE FROM books WHERE bookID = :bookID", {'bookID': bookID})
            print(f"Book with ID {bookID} has been removed.")


    def add_book(self):
        bookID = input("Enter book ID: ")
        self.cursor.execute("SELECT * FROM books WHERE bookID = :bookID", {'bookID': bookID})
        book = self.cursor.fetchone()
        if book:
            print(f"Book with ID {bookID} is already in the table.")
            return
        title = input("Enter book title: ")
        authors = input("Enter book authors: ")
        average_rating = float(input("Enter book average rating: "))
        isbn = int(input("Enter book ISBN: "))
        isbn13 = int(input("Enter book ISBN13: "))
        language_code = input("Enter book language code: ")
        num_pages = int(input("Enter book number of pages: "))
        ratings_count = int(input("Enter book ratings count: "))
        text_reviews_count = int(input("Enter book text reviews count: "))
        publication_date = input("Enter book publication date: ")
        publisher = input("Enter book publisher: ")
        Available = input("Leave column empty: ")
        with self.conn:
            self.cursor.execute("INSERT INTO books VALUES (:bookID, :title, :authors, :average_rating, :isbn, :isbn13, :language_code, :num_pages, :ratings_count, :text_reviews_count, :publication_date, :publisher, :Empty)", {'bookID': bookID, 'title': title, 'authors':authors, 'average_rating':average_rating, 'isbn':isbn, 'isbn13':isbn13, 'language_code':language_code, 'num_pages':num_pages, 'ratings_count':ratings_count, 'text_reviews_count':text_reviews_count, 'publication_date':publication_date, 'publisher':publisher, 'Available':Available })
    
    
    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        if not books:
            print("No books found.")
        else:
            print("All books:")
            for book in books:
                print(book)

    
    
    def remove_user(self):
        userid = input("Enter user ID: ")
        with self.konn:
            self.kursor.execute("DELETE FROM login WHERE userid = :userid", {'userid': userid})
        print(f"User with ID {userid} and their password have been removed from login.")
    
    def remove_studentlogindetails(self):
        student_id = input("Enter student_ID: ")
        with self.donn:
            self.dursor.execute("DELETE FROM studentlogin WHERE student_id = :student_id", {'student_id': student_id})
        print(f"User with ID {student_id} and their student_access_code have been removed from studentlogin.")
    
    def remove_stafflogindetails(self):
        staff_id = input("Enter staff_ID: ")
        with self.fonn:
            self.fursor.execute("DELETE FROM stafflogin WHERE staff_id = :staff_id", {'staff_id': staff_id})
        print(f"User with ID {staff_id} and their staff_access_code have been removed from stafflogin.")
    
    def remove_externaluserdetails(self):
        externaluser_id = input("Enter externaluser_id: ")
        with self.jonn:
            self.jursor.execute("DELETE FROM externaluserlogin WHERE externaluser_id = :externaluser_id", {'externaluser_id': externaluser_id})
        print(f"externaluser with ID {externaluser_id} and their externaluser_access_code have been removed from externaluserlogin.")
        
    def get_all_users(self):
        self.cursor.execute("SELECT userid FROM login")
        users = self.kursor.fetchall()
        if not users:
            print("No users found.")
        else:
            print("All user IDs:")
            for user in users:
                print(user[0])
    
    def addto_user(self):
        userid = input("Enter user ID: ")
        password = input("Enter user password: ")
        with self.konn:
            self.kursor.execute("INSERT INTO login(userid, password) VALUES (:userid, :password)", {'userid': userid, 'password': password})
            print(f"User with ID {userid} and password has been added to the login table.")
            
    def addto_studentlogin(self):
        student_id = input("Enter user student_id: ")
        student_access_code = input("Enter user student_access_code: ")
        with self.donn:
            self.dursor.execute("INSERT INTO studentlogin(student_id, student_access_code) VALUES (:student_id, :student_access_code)", {'student_id': student_id, 'student_access_code': student_access_code})
            print(f"Student with ID {student_id} and student_access_code has been added to the studentlogin table.")
            
    def addto_stafflogin(self):
        staff_id = input("Enter user staff_id: ")
        staff_access_code = input("Enter user staff_access_code: ")
        with self.fonn:
            self.fursor.execute("INSERT INTO stafflogin(staff_id, staff_access_code) VALUES (:staff_id, :staff_access_code)", {'staff_id': staff_id, 'staff_access_code': staff_access_code})
            print(f"Staff with ID {staff_id} and staff_access_code has been added to the stafflogin table.")
            
    def addto_externaluserlogin(self):
        externaluser_id = input("Enter user externaluser_id: ")
        externaluser_access_code = input("Enter user externaluser_access_code: ")
        with self.jonn:
            self.jursor.execute("INSERT INTO externaluserlogin(externaluser_id, externaluser_access_code) VALUES (:externaluser_id, :externaluser_access_code)", {'externaluser_id': externaluser_id, 'externaluser_access_code': externaluser_access_code})
            print(f"externaluser with ID {externaluser_id} and externaluser_access_code has been added to the externaluserlogin table.")
    
            
    def issue_book(self):
        isbn = input("Enter isbn: ")
        userid = input("Enter userID: ")
        self.cursor.execute("SELECT * FROM books WHERE isbn = :isbn", {'isbn': isbn})
        book = self.cursor.fetchone()
        if not book:
            print(f"Book with ID {isbn} is not available.")
            return
        if book[-2] == 0:
            print(f"Book with ID {isbn} is not available for issuance.")
            return
        self.kursor.execute("SELECT * FROM login WHERE userid = :userid", {'userid': userid})
        user = self.kursor.fetchone()
        if not user:
            print(f"user with ID {userid} is not available.")
            return
        with self.conn:
            self.cursor.execute("UPDATE books SET available = 0 WHERE isbn = :isbn", {'isbn': isbn})
            print(f"Book with isbn {isbn} has been issued to student with ID {userid}.")
            
    def get_book(self):
        bookID = input("Enter book ID: ")
        self.cursor.execute("SELECT * FROM books WHERE bookID = :bookID", {'bookID': bookID})
        book = self.cursor.fetchone()
        if not book:
            print(f"Book with ID {bookID} is not available.")
            return
        print(f"Book details: {book}")

   

    def impose_fine(self):
        userID = input("Enter user ID: ")
        bookID = input("Enter book ID: ")
        issueDate_str = input("Enter issue date in the format YYYY-MM-DD: ")
        issueDate = datetime.datetime.strptime(issueDate_str, "%Y-%m-%d").date()
        returnDate_str = input("Enter return date in the format YYYY-MM-DD or press enter if book not yet returned: ")
        returnDate = None if returnDate_str == "" else datetime.datetime.strptime(returnDate_str, "%Y-%m-%d").date()
        current_date_str = input("Enter current date in the format YYYY-MM-DD : ")
        current_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d").date()
        if returnDate is None:
            if (current_date - issueDate).days > 7:
                fine = (current_date - issueDate).days * 0.3
                print(f"User with ID {userID} has not returned book with ID {bookID} and a fine of {fine} has been imposed.")
            else:
                print(f"User with ID {userID} has not returned book with ID {bookID} but the due date has not yet passed.")
        else:
            if (returnDate - issueDate).days > 7:
                fine = (returnDate - issueDate).days * 0.3
                print(f"User with ID {userID} has returned book with ID {bookID} after the due date and a fine of {fine} has been imposed.")
            else:
                print(f"User with ID {userID} has returned book with ID {bookID} within the due date.")






if __name__ == '__main__':
    librarian = Librarian()
    librarian.onStart()

    

