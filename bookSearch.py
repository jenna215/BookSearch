import requests

# Document formatted with Black Formatter
# Establish class for main function to access
class Books:
    def __init__(self, source):
        self.source = source

# Incorporate functions to call for tasks of searching through google books api, 
# adding books to list, and showing books on list.
# Includes checking for connection status and multiple user inputs.

    def searchBookinAPI(self):
        bookTitle = input("Please enter book title: ")
        apiKey = "AIzaSyADNDAyuS4aq8m_oc6ha1r0sXI25ziZCl4"
        responseGoogle = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q=intitle:{bookTitle}&key={apiKey}"
        )
        if responseGoogle.status_code != 200:
            raise ConnectionError("Problem with connecting to given URL")
        else:
            data = responseGoogle.json()
            if "items" in data:
                for item in data["items"][0:5]:
                    title = item["volumeInfo"]["title"]
                    author = item["volumeInfo"]["authors"]
                    if "publisher" in item["volumeInfo"]:
                        publisher = item["volumeInfo"]["publisher"]
                    else:
                        publisher = "Unknown Publisher"
                    break
                print(f"\nTitle: {title}\nAuthor: {author}\nPublisher: {publisher}\n")

# I attempted to connect to another helper function to tidy the rest of this function's code, 
# but the "title, author, publisher" variables caused issues with connection. 
# and the second "else" statement was gray... ("addDecision" function can be seen at the bottom)
                # bookManager = Books("./Data/bookData.txt")
                # bookManager.addDecision()

# option to add search result to book list
                while True:
                    decision = input(
                        "Do you want to add this position to your shelf? [y/n]: "
                    )
                    if decision == "y":
                        self.addBook(title, author, publisher)
                        break
                    elif decision == "n":
                        break
                    else:
                        print("Unknown symbol, type y or n")
            else:
                print("Sorry, we do not have this title in our API")
                return

# append search result to a txt file 
    def addBook(self, title, author, publisher):
        with open('./Data/bookData.txt', 'a') as f:
            f.write(f"\nTitle: {title}\nAuthor: {author}\nPublisher: {publisher}\n")
        print("Your book has been added to your Bookshelf \n")

# read txt file for complete list of added books
    def showBooks(self):
        with open('./Data/bookData.txt', 'r') as f:
            data = f.read()
            print(data)



    # def addDecision(self):
    #     while True:
    #         decision = input(
    #             "Do you want to add this position to your shelf? [y/n]: "
    #         )
    #         if decision == "y":
    #             self.addBook(title, author, publisher)
    #             break
    #         elif decision == "n":
    #             break
    #         else:
    #             print("Unknown symbol, type y or n")
    #     else:
    #         print("Sorry, we do not have this title in our API")
    #         return