import unittest

from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith checks out the new app
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do lists', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

       # She types 'Buy featers' into a text box

        # When she hits enter the page updates and now the page lists her first item

        # There is stll a text box inviting her to add another item

        # The page updates again and now shows both items

        # Edith wonders if the site will remember hir lists.   She
        # the site has generated a unique URL for here -- there is some
        # explanatory text around this point

        # She visits that URL - her to-do lsit is still there.

        # Satisfiied, she goes back to sleep

if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    unittest.main()
