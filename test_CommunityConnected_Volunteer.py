import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_ll(self):
        user = "testuser"
        pwd = "maverick1a"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://byronwebapps.pythonanywhere.com/accounts/login/")
        elem = driver.find_element_by_name("username")
        elem.send_keys(user)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pwd)
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        try:
            driver.get("https://byronwebapps.pythonanywhere.com/profile")
            time.sleep(5)
            driver.get("https://byronwebapps.pythonanywhere.com/search_organizations/")
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/form/button").click()
            time.sleep(5)
            driver.get("https://byronwebapps.pythonanywhere.com/")
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div/div/div[1]/ul[1]/li[3]/a").click()
            time.sleep(5)
            driver.get("https://byronwebapps.pythonanywhere.com/search_organizations/")
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/form/button").click()
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/ul/li/a").click()
            time.sleep(5)


            assert True

        except NoSuchElementException:
            self.fail("Volunteer features are not fully working")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()