from selenium.common.exceptions import NoSuchElementException
from alfa_lib import *


class Navigate(object):

    def __init__(self, driver):
        self.driver = driver

    def sort_list(self, how, desc=True):
        self.driver.find_element_by_xpath(sort_order).click()
        self.driver.find_element_by_xpath(how).click()
        if desc:
            self.driver.find_element_by_xpath(sort_descending).click()
        else:
            self.driver.find_element_by_xpath(sort_ascending).click()

    def buy(self, position):
        self.driver.find_element_by_xpath("("+buy_item+")["+str(position)+"]").click()

    def basket(self):
        print(self.driver.find_element_by_xpath(cart).click())

    def check_basket_item(self, qty):
        assert self.driver.find_element_by_xpath(cart).text[0:4] == qty

