from bookSearch import *
import sys


def main():
# CLI UI with choices for using Google Books API
# Currently, only 1 and 3 work...
    choice = 0
    while choice != 3:
        print("***Books Manager***")
        print("1) Lookup a Book")
        print("2) Display Your Book List")
        print("3) Quit")
        choice = input()
# choice 1 connects to searchBookinAPI function in Books class in bookSearch.py
# to return the first result of your book's title, author, and publisher. 
        if choice == "1":
            print("Looking up a book...")
            bookManager = Books("./Data/bookData.json")
            bookManager.searchBookinAPI()
# Having an issue here with connecting. Looking forward to feedback and suggestions.
        elif choice == "2":
            print("Displaying all books...")
            bookManager = Books("./Data/bookData.json")
            bookManager.showBooks()
# Uses sys module to quit program after finished viewing search results. 
        else:
            print("Quitting Program...")
            sys.exit("Program Terminated!")


if __name__ == "__main__":
    main()
