from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.alfa.cz/")
driver.find_element_by_link_text(u"Pevné disky a SSD").click()
driver.find_element_by_name("SortOrder").click()
driver.find_element_by_xpath("//option[@value='4']").click()
driver.find_element_by_xpath(u"//img[@alt='Seřadí položky sestupně (Z-A, 10-1)']").click()
driver.find_element_by_name("buy").click()
driver.find_element_by_xpath("(//input[@name='buy'])[2]").click()
driver.find_element_by_xpath("//td[@id='topbasket']/a/img").click()