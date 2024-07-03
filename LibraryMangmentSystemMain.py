import os
import sys
import datetime
#This is practice Project to understand how Mangment system are bulit


class LCM:
    """The class for my Library Mangment System"""
    def __init__(self,library_doc,library_name):
        self.library_doc = library_doc
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(os.path.join(sys.path[0], self.library_doc)) as bks:
            list_of_books = bks.readlines()
        for line in list_of_books:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
                    "lender_name":"","Issue_Date":"","Status": "Available"}})
            Id += 1
    def display_books(self):
        print(" ------------------------------ List of Books ------------------------------")
        print("Books ID", "\t", "Title")
        print("----------------------------------------------------------------------------")
        for key,value in self.books_dict.items():
            print(key,'\t\t',value.get("books_title"), "- [",value.get("books_title"),"]" )
    #Method to Issue a book ------------------------
    def Issue_books(self):
        books_id = input("Enter books ID: ")

        current_date = datetime.datetime.now().strftime("%Y-%m_%D %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['Status'] == "Available":
                print("The book is already issued to {1} on {2} ".format(self.books_dict[books_id]['lender_name'],self.books_dict[books_id]["Issue_Data"]))
                return self.Issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
                lender_name = input("Enter your name to issue book: ")
                self.books_dict[books_id]['lender_name'] = lender_name
                self.books_dict[books_id]['Issue_Date'] = current_date
                self.books_dict[books_id]['Status'] = "Unavailable"
                print("The book {} was Issued on {} by {}".format(self.books_dict[books_id]['books_title'],self.books_dict[books_id]['Issue_Date'],self.books_dict[books_id]['lender_name']))
        else:
            print("There exist No book with that Id: {1}".format(books_id))
            return self.Issue_books
    #Add book method --------------------------------
    def add_books(self):
        new_book = input("Enter books title: ")
        #Assuming that the users has added somthing to library
        if new_book == "":
            return self.add_books
        elif len(new_book) > 30:
            print("The books title is to long!!!!")
            self.add_books()
        else:
            with open(self.library_doc,"a") as bk:
                bk.writelines(f"{new_book}\n")
                newId = int(max(list(self.books_dict.keys()))) + 1
                self.books_dict.update({str(newId) : {"books_title":new_book,
                    "lender_name":"","Issue_Date":"","Status": "Available"}})
                print(f"This books '{new_book}' has been added successfully!")
    #return books method --------------------------------
    def return_books(self):
        book_id = input("Please enter the book you are returning ID: ")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]["Status"] == "Available":
                print("This book is already available")
                return self.return_books()
            if not self.books_dict[book_id]["Status"] == "Available":
                self.books_dict[book_id]["lender_name"] = ""
                self.books_dict[book_id]["Issue_Date"] = ""
                self.books_dict[book_id]["Status"] = "Available"
                print("Thank you for returning the book !!!")
            else:
                print("Book Id not Found")


# tryed using the tryed function can't get it to work for some reason thought                

try:
    myLCMs = LCM("books.txt","Python Library")
    press_key_list = {"D": "Display Books", "I":"Issue Books", "A":"Add Books","R":"Return Books","Q":"Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n---------------------- Welecome To {myLCMs.library_name} manangement System ---------------------- \n")
        for key,value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\n Current Selection : Issue Books")
            myLCMs.Issue_books()
        elif key_press == "a":
            print("\nCurrent Selection : Add Book\n")
            myLCMs.add_books()
        elif key_press == "d":
            print("\nCurrent Selection : Display Books\n")
            myLCMs.display_books()
        elif key_press == "r":
            print("\nCurrent Selection : Return Books\n")
            myLCMs.return_books()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print("Somthing went Worng!!!!")