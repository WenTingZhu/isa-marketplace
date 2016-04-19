import os, unittest
# from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


# Before building ensure that you have the most recent chromedriver available on your $PATH.
# https://sites.google.com/a/chromium.org/chromedriver/downloads
chromedriver = "/home/wzhu/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
# # driver = webdriver.Chrome(chromedriver)
# # driver.get('http://seleniumhq.org/')
#
# browser = webdriver.Chrome(chromedriver)
# browser.get('http://www.yahoo.com')
# assert 'Yahoo' in browser.title
#
# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)

"""
class GeneralTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver)
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://localhost:8002/')
        self.assertIn('Rideshare - Share Rides and Stuff', self.browser.title)
"""

class AccountsTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chromedriver)
        self.addCleanup(self.driver.quit)

    def testh1(self):
        self.driver.get('http://localhost:8002/')
        # find the element with name attribute
        self.assertEquals("RideShare", str(self.driver.find_element_by_id("h1").text))

    def testcreateUser(self):
        self.driver.get('http://localhost:8002/')
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id("signup_email").is_displayed())
        actions = ActionChains(self.driver)
        signup_email = self.driver.find_element_by_id("signup_email")
        actions.move_to_element(signup_email).click()
        actions.send_keys("1@gmail.com").perform()
        signup_password = self.driver.find_element_by_id("signup_pwd")
        actions.move_to_element(signup_password).click()
        actions.send_keys("1").perform()
        actions = ActionChains(self.driver)
        signup_firstname = self.driver.find_element_by_id("signup_firstname")
        actions.move_to_element(signup_firstname).click()
        actions.send_keys("1").perform()
        signup_lastname = self.driver.find_element_by_id("signup_lastname")
        actions.move_to_element(signup_lastname).click()
        actions.send_keys("1").perform()
        actions = ActionChains(self.driver)
        signup_phone = self.driver.find_element_by_id("signup_phone")
        actions.move_to_element(signup_phone).click()
        actions.send_keys("1").perform()
        signup_school = self.driver.find_element_by_id("signup_school")
        actions.move_to_element(signup_school).click()
        actions.send_keys("1").perform()
        # submit the form
        self.driver.find_element_by_id("signup-btn").click()
        self.assertIn('Rideshare - Share Rides and Stuff', self.driver.title)

    def testlogIn(self):
        self.driver.get('http://localhost:8002/')
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id("login_email").is_displayed())
        actions = ActionChains(self.driver)
        login_email = self.driver.find_element_by_id("login_email")
        actions.move_to_element(login_email).click()
        actions.send_keys("1@gmail.com").perform()
        login_password = self.driver.find_element_by_id("login_password")
        actions.move_to_element(login_password).click()
        actions.send_keys("1").perform()
        # submit the form
        self.driver.find_element_by_id("login-btn").click()

        self.assertIn('Rideshare - Share Rides and Stuff', self.driver.title)


class SearchTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chromedriver)
        self.addCleanup(self.driver.quit)

    def testBlankSearch(self):
        self.driver.get('http://localhost:8002/')
        self.driver.find_element_by_id("search_btn").click()
        self.assertEquals('', self.driver.title)

    def testSearch(self):
        self.driver.get('http://localhost:8002/')
        actions = ActionChains(self.driver)
        toClick = self.driver.find_element_by_id("search_query")
        actions.move_to_element(toClick).click()
        actions.send_keys("1@gmail.com").perform()
        self.driver.find_element_by_id("search_btn").click()
        self.assertEquals('Rideshare - Search Results', self.driver.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
