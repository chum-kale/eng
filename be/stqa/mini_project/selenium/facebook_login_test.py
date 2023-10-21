from selenium import webdriver
import unittest
import os

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Create a new Firefox profile if it doesn't exist
        profile_dir = os.path.join(os.environ["HOME"], ".mozilla/firefox/profiles/test")
        if not os.path.exists(profile_dir):
            os.mkdir(profile_dir)

        # Create a new Firefox driver using the test profile
        self.driver = webdriver.Firefox(profile_directory=profile_dir)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://www.facebook.com/login")

        # Enter the username and password
        username_field = self.driver.find_element_by_id("email")
        username_field.send_keys("your_username")

        password_field = self.driver.find_element_by_id("pass")
        password_field.send_keys("your_password")

        # Click the login button
        login_button = self.driver.find_element_by_id("loginbutton")
        login_button.click()

        # Verify that the user was successfully logged in
        expected_title = "Facebook"
        actual_title = self.driver.title
        self.assertEqual(actual_title, expected_title)

        # Assert that the error message is displayed
        error_message = self.driver.find_element_by_class_name("error")
        self.assertEqual(error_message.text, "Incorrect Email or Password")

        # Assert that the "Reset Your Password" link is displayed
        reset_password_link = self.driver.find_element_by_link_text("Reset Your Password")
        self.assertTrue(reset_password_link.is_displayed())


if __name__ == "__main__":
    unittest.main()
