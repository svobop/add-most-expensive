from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from alfa import Navigate
from alfa_lib import *

class AddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_to_cart(self):
        driver = self.driver
        driver.get(front_page)
        driver.find_element_by_xpath(subcat_hdd_ssd).click()

        navigate = Navigate(driver)

        navigate.sort_list(sort_option_price)

        navigate.buy(1)
        navigate.buy(2)

        navigate.check_basket_item("2 ks")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
