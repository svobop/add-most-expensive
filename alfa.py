from selenium.common.exceptions import NoSuchElementException


class Navigate(object):

    def __init__(self, driver):
        self.driver = driver

    def category(self, category):
        self.driver.find_element_by_link_text(category).click()

    def sort_list(self, how, desc=True):
        # how options
        option_value = {"pid": "1",
                        "name": "2",
                        "description": "3",
                        "price": "4",
                        "popularity": "5",
                        "recommended": "6"}
        self.driver.find_element_by_name("SortOrder").click()
        self.driver.find_element_by_xpath("//option[@value='" + option_value[how] + "']").click()
        if desc:
            self.driver.find_element_by_xpath(u"//img[@alt='Seřadí položky sestupně (Z-A, 10-1)']").click()
        else:
            self.driver.find_element_by_xpath(u"//img[@alt='Seřadí položky vzestupně (A-Z, 1-10)']").click()

    def buy(self, position):
        self.driver.find_element_by_xpath("(//input[@name='buy'])["+str(position)+"]").click()

    def basket(self):
        self.driver.find_element_by_xpath("//td[@id='topbasket']/a/img").click()

    def check_basket_item(self, position):
        try:
            self.driver.find_element_by_xpath("/html/body/div/div[5]/div[4]/form["+str(position)+"]")
        except NoSuchElementException:
            raise Exception("basket item is missing")