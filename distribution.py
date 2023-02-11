from student import Student
from librarian import Librarian
from staff import Staff
from externaluser import Externaluser




flag = False

def check_flag():
    if flag:
        distribution = Distribution()
        distribution.onFaith()
    else:
        print("Please login or register first")

class Distribution():
    def __init__(self):
        pass

    def onFaith(self):
        while True:
            print("===============================")
            print(" Library Management System ")
            print("-------------------------------")
            print("Select an option:")
            print("1. Student")
            print("2. Staff")
            print("3. External User")
            print("q. Quit")
            user_input = input("Enter your choice: ")
            if user_input == "1":
                student = Student()
                student.onStart()
                student.conn.close()
            elif user_input == "2":
                staff = Staff()
                staff.onStart()
                staff.conn.close()
            elif user_input == "3":
                externaluser = Externaluser()
                externaluser.onStart()
                externaluser.conn.close()
            elif user_input == "q":
                print("Bye..")
                break
            else:
                print("Invalid input. Please try again.")

# Here you check if the user has logged in or registered before calling the Distribution class
check_flag()


























# class Distribution():
#     def __init__(self):
#         pass


#     def onFaith(self):
#         while True:
#             print("===============================")
#             print(" Library Management System ")
#             print("-------------------------------")
#             print("Select an option:")
#             print("1. Student")
#             print("2. Staff")
#             print("3. External User")
#             print("4. Librarian")
#             print("q. Quit")
#             user_input = input("Enter your choice: ")
#             if user_input == "1":
#                 student = Student()
#                 student.onStart()
#                 student.conn.close()
#             elif user_input == "2":
#                 librarian = Librarian()
#                 librarian.onStart()
#                 librarian.conn.close()
#             elif user_input == "3":
#                 staff = Staff()
#                 staff.onStart()
#                 staff.conn.close()
#             elif user_input == "4":
#                 externaluser = Externaluser()
#                 externaluser.onStart()
#                 externaluser.conn.close()
#             elif user_input == "q":
#                 print("Bye..")
#                 break
#             else:
#                 print("Invalid input. Please try again.")


# # Create an instance of the Distribution class and call the onFaith() method
# distribution = Distribution()
# distribution.onFaith()
