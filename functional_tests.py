import unittest # Import the unittest module
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# --- Configuration for GeckoDriver (adjust path as needed) ---
# IMPORTANT: Replace with the ACTUAL full path to your geckodriver executable
# Example for Windows: geckodriver_path = 'C:/path/to/your/geckodriver.exe'
# Example for macOS/Linux: geckodriver_path = '/usr/local/bin/geckodriver'
# If geckodriver is in your system PATH, you can set this to None or remove this block
geckodriver_path = None # Set to your path if not in system PATH
# --- End Configuration ---

# Define a test class that inherits from unittest.TestCase
class NewVisitorTest(unittest.TestCase):

    # setUp method runs before each test method (e.g., test_can_start_a_todo_list)
    def setUp(self):
        # Initialize the browser. If geckodriver_path is set, use it.
        if geckodriver_path:
            service = Service(executable_path=geckodriver_path)
            self.browser = webdriver.Firefox(service=service)
        else:
            self.browser = webdriver.Firefox() # Assumes geckodriver is in system PATH

    # tearDown method runs after each test method
    def tearDown(self):
        self.browser.quit() # Quits the browser automatically

    # This is our first functional test method. Test methods must start with 'test_'
    def test_can_start_a_todo_list(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        # Using self.assertIn for better error messages
        self.assertIn("To-Do", self.browser.title)

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Satisfied, she goes back to sleep

        # Fail the test intentionally to mark it as unfinished, as per the tutorial
        self.fail("Finish the test!")

# This block ensures that unittest.main() is called when the script is run directly
if __name__ == "__main__":
    unittest.main()
