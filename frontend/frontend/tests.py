import os, unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

class TestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver)
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://localhost:8002/')
        self.assertIn('Rideshare - Share Rides and Stuff', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
