import json
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
        responseGoogle = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q=intitle:{bookTitle}&maxResults=5&key=AIzaSyADNDAyuS4aq8m_oc6ha1r0sXI25ziZCl4"
        )
        if responseGoogle.status_code != 200:
            raise ConnectionError("Problem with connecting to given URL")
        else:
            data = responseGoogle.json()
            if "items" in data:
                for item in data["items"]:
                    title = item["volumeInfo"]["title"]
                    author = item["volumeInfo"]["authors"]
                    if "publisher" in item["volumeInfo"]:
                        publisher = item["volumeInfo"]["publisher"]
                    else:
                        publisher = "Unknown Publisher"
                    break
                print(f"\nTitle: {title}\nAuthor: {author}\nPublisher: {publisher}\n")

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

# Everything works pretty well until this point. 
# The json file doesn't connect and load the addBook data.
    def addBook(self, title, author, publisher):
        data = {}
        with open('./Data/bookData.json', 'a') as f:
            temp = json.load(f)
        data["title"] = title
        data["author"] = author
        data["publisher"] = publisher
        temp.append(data)
        with open(self.source, "w") as f:
            json.dump(temp, f)
        print("Your book has been added to your Bookshelf ")

    def showBooks(self):
        f = open('./Data/bookData.json', 'r')
        data = f.read()
        print(data)
        bookLoad = json.load(data)
        print(bookLoad)
        while True:
            decision = input(
        "Do you want to add this position to your shelf? [y/n]: "
    )
            if decision == "y":
                bookManager = Books("./Data/bookData.json")
                bookManager.searchBookinAPI()
                break
            elif decision == "n":
                break
