import unittest
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FirefoxSearch(unittest.TestCase):

    """
    This test class contains test cases for searching on the Python.org website using Firefox.
    """

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):

        """
        This test case verifies that the user can search for the term "getting started with python" on the Python.org website
        and be taken to the correct search results page.
        """

        driver = self.driver
        driver.get("https://www.python.org")

        # Find the search bar element
        elem = driver.find_element_by_name("q")

        # Enter the search term
        elem.send_keys("getting started with python")

        # Submit the search form
        elem.send_keys(Keys.RETURN)

        # Verify that the user is taken to the correct search results page
        assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == driver.current_url

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
