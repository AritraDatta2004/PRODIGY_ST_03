#Task ST_03



import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLogin(unittest.TestCase):

    def setUp(self):
        """
        This method is called before each test.
        It initializes the WebDriver and navigates to the login page.
        """
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        time.sleep(2) # Allow time for the page to load

    def test_positive_login(self):
        """
        Test Case 01: Positive Login
        This test verifies that a user with valid credentials can successfully log in.
        """
        # Find the username and password fields and enter the credentials
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Verify that the login was successful by checking the URL
        expected_url = "https://www.saucedemo.com/inventory.html"
        self.assertEqual(self.driver.current_url, expected_url, "Login was not successful.")
        print("Positive Login Test: Passed")

    def test_negative_invalid_password(self):
        """
        Test Case 02: Negative Login - Invalid Password
        This test verifies that the system prevents login with a valid username but an invalid password.
        """
        # Find the username and password fields and enter the credentials
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("wrong_password")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Verify that an error message is displayed
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        expected_error = "Epic sadface: Username and password do not match any user in this service"
        self.assertIn(expected_error, error_message, "Error message for invalid password was not displayed correctly.")
        print("Negative Login Test (Invalid Password): Passed")

    def test_negative_locked_out_user(self):
        """
        Test Case 03: Negative Login - Locked Out User
        This test verifies that a user who is locked out cannot log in.
        """
        # Find the username and password fields and enter the credentials
        self.driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Verify that an error message for a locked-out user is displayed
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        expected_error = "Epic sadface: Sorry, this user has been locked out."
        self.assertIn(expected_error, error_message, "Error message for locked out user was not displayed correctly.")
        print("Negative Login Test (Locked Out User): Passed")

    def test_negative_empty_credentials(self):
        """
        Test Case 04: Negative Login - Empty Credentials
        This test verifies that the system prompts for a username if the fields are left empty.
        """
        # Click the login button without entering any credentials
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Verify that an error message for a required username is displayed
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        expected_error = "Epic sadface: Username is required"
        self.assertIn(expected_error, error_message, "Error message for empty credentials was not displayed correctly.")
        print("Negative Login Test (Empty Credentials): Passed")

    def tearDown(self):
        """
        This method is called after each test.
        It closes the browser window.
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
