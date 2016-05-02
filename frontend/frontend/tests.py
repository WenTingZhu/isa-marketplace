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


# Generic test case
class GeneralTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver)
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://localhost:8002/')
        self.assertIn('Rideshare - Share Rides and Stuff', self.browser.title)


# Test case for accounts
class AccountsTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chromedriver)
        self.addCleanup(self.driver.quit)


    def testh1(self):
        self.driver.get('http://localhost:8002/')
        # find the element with name attribute
        self.assertEquals("RideShare", str(self.driver.find_element_by_id("h1").text))

    # Need to manually click on Sign up button for test case to work
    def testcreateUser(self):
        self.driver.get('http://localhost:8002/')
        WebDriverWait(self.driver, 15).until(lambda s: s.find_element_by_id("signup-btn").is_displayed())
        actions = ActionChains(self.driver)
        signup_email = self.driver.find_element_by_id("signup_email")
        actions.move_to_element(signup_email).click()
        actions.send_keys("1@gmail.com")
        signup_password = self.driver.find_element_by_id("signup_pwd")
        actions.move_to_element(signup_password).click()
        actions.send_keys("1")
        signup_firstname = self.driver.find_element_by_id("signup_firstname")
        actions.move_to_element(signup_firstname).click()
        actions.send_keys("1")
        signup_lastname = self.driver.find_element_by_id("signup_lastname")
        actions.move_to_element(signup_lastname).click()
        actions.send_keys("1")
        signup_phone = self.driver.find_element_by_id("signup_phone")
        actions.move_to_element(signup_phone).click()
        actions.send_keys("1")
        signup_school = self.driver.find_element_by_id("signup_school")
        actions.move_to_element(signup_school).click()
        actions.send_keys("1").perform()
        # submit the form
        self.driver.find_element_by_id("signup-btn").click()
        self.assertIn('Rideshare - Share Rides and Stuff', self.driver.title)


    # Need to manually click on Log in button for test case to work
    def testlogIn(self):
        self.driver.get('http://localhost:8002/')
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id("login-btn").is_displayed())
        actions = ActionChains(self.driver)
        login_email = self.driver.find_element_by_id("login_email")
        actions.move_to_element(login_email).click()
        actions.send_keys("1@gmail.com")
        login_password = self.driver.find_element_by_id("login_password")
        actions.move_to_element(login_password).click()
        actions.send_keys("1").perform()
        # submit the form
        self.driver.find_element_by_id("login-btn").click()

        self.assertIn('Rideshare - Dashboard', self.driver.title)


# Test case for create ride
class CreateRideTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chromedriver)
        self.addCleanup(self.driver.quit)

    def testCreateRideButton(self):
        self.driver.get('http://localhost:8002/')
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id("login_email").is_displayed())
        actions = ActionChains(self.driver)
        login_email = self.driver.find_element_by_id("login_email")
        actions.move_to_element(login_email).click()
        actions.send_keys("1@gmail.com")
        login_password = self.driver.find_element_by_id("login_password")
        actions.move_to_element(login_password).click()
        actions.send_keys("1").perform()
        # submit the form
        self.driver.find_element_by_id("login-btn").click()
        self.driver.find_element_by_link_text("Create a New Ride").click()
        self.assertEquals('Rideshare - Create Ride', self.driver.title)

    def testCreateRide(self):
        self.driver.get('http://localhost:8002/')
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id("login_email").is_displayed())
        actions = ActionChains(self.driver)
        login_email = self.driver.find_element_by_id("login_email")
        actions.move_to_element(login_email).click()
        actions.send_keys("1@gmail.com")
        login_password = self.driver.find_element_by_id("login_password")
        actions.move_to_element(login_password).click()
        actions.send_keys("1").perform()
        # submit the form
        self.driver.find_element_by_id("login-btn").click()
        self.driver.find_element_by_link_text("Create a New Ride").click()

        actions = ActionChains(self.driver)
        open_seats = self.driver.find_element_by_id("open_seats")
        actions.move_to_element(open_seats).click()
        actions.send_keys("1")
        departure_time = self.driver.find_element_by_id("departure_time")
        actions.move_to_element(departure_time).click()
        actions.send_keys(Keys.ARROW_LEFT).send_keys(Keys.ARROW_LEFT).send_keys(Keys.ARROW_LEFT)
        self.driver.implicitly_wait(10)
        actions.send_keys("11112011\t1111AM").send_keys(Keys.ARROW_LEFT).perform()
        self.driver.find_element_by_id("create_ride_btn").click()
        self.assertEquals('Rideshare - Ride Detail', self.driver.title)


# Test case for search
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
