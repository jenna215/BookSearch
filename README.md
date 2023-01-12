# Book Search

Use Google API to search for books.

**Python Version**: 3.10.9
\
**Modules Used**: 
* import sys
* import requests \
*(use "pip install requests" or "python -m pip install requests" in your terminal to install "requests" module)*
* import pytest \
*(use "pip install -U pytest" in your terminal to install "pytest" module)*
\

**Test Used:**
* import unittest *(**to run tests**, enter in terminal: "python -m unittest tests.py")*
* * *Test included: Checks if it is True that the status code coming from the Google Books API is OK*

**To Run Repository**
* At https://github.com/jenna215/BookSearch click green "<> Code" button 

* "Download ZIP", then unzip and open file in terminal from bookSearch folder directory 
\
*(Tip: Open File Explorer to desired folder and type "cmd" in the directory path bar to open the folder's code in your terminal)*
* After "BookSearch>" enter "python main.py" to initiate program

## Current suggested functional path:
 * Starting from bookSearch>python main.py
 * 1 (Look up a book)
 * Enter your book title\
 Options:
 * y (add book to shelf)
 * n (do not add to shelf and keep searching)
 * 1 again to search for another book, 2 to view your list, or 3 to quit.\
 
 *bookData.txt includes a few books from a result of experimenting with the program. Feel free to view current list and add your own books.\
 Currently, books can be manually deleted in the bookData.txt file.*

## Successes:
Connected Google Books API, functional searching through Command Line Interface, and adding books to local .txt file.

## Resources used: 
* YouTube
* GitHub
* StackOverflow

## Functions I would add with more time:
* Showing 5 Google Books search results and choosing which one to add to a book list.
* * I had found some things that could be potentially helpful, such as going through a [0:5] range with ['items'], and using &maxResults=5, but they didn't work out in my code, so I would need more time to make it work.
* Option to delete books from list using CLI. 
* * Maybe I could use a pop() method.
* Study unittest more and run more tests.