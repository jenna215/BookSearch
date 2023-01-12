import unittest
from bookSearch import *
from main import *

# checks if it is True that the status code coming from the Google Books API is OK

class TestSearchBookinAPI(unittest.TestCase): 
    def test_SearchBookinAPI(self):
        apiKey = "AIzaSyADNDAyuS4aq8m_oc6ha1r0sXI25ziZCl4"
        responseGoogle = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?&key={apiKey}"
        )
        responseGoogle.status_code == 200

        self.assertTrue(responseGoogle.status_code)
        


if __name__ == '__main__':
    unittest.main()