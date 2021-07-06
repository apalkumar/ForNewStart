import time
from selenium.webdriver.common.by import By

from utility.BaseClass import BaseClass


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    ProductSearchBox = (By.CSS_SELECTOR, "input.search-keyword")
    SearchedItem = (By.XPATH, "//div[@class='product-action']/button")
    Searchtext = (By.XPATH, "//parent::div/parent::div/h4")
    cart = (By.XPATH, "//a[@class='cart-icon']")
    proceedtocheckout = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    # Top_Deal = (By.XPATH, "//a[text()='Top Deals']")
    Top_Deal = (By.LINK_TEXT, "Top Deals")
    Top_Deal_Search = (By.XPATH, "//input[@id='search-field']")
    logN = BaseClass()

    def SearchProduct(self):
        return self.driver.find_element(*HomePage.ProductSearchBox)

    def count(self):
        count = len(self.driver.find_elements_by_xpath("//div[@class='products']/div"))
        HomePage.logN.getlogger().info("Count Inside Method is-->"+str(count))
        return count

    def proceed_checkout(self):
        list = []
        SearchedItems = self.driver.find_elements(*HomePage.SearchedItem)
        HomePage.logN.getlogger().info("WE are inside of the MEthod")

        for search in SearchedItems:
            # list.append(search.Searchtext.text)
            list.append(search.find_element_by_xpath("parent::div/parent::div/h4"))
            search.click()
            time.sleep(1)

        self.driver.find_element(*HomePage.cart).click()
        self.driver.find_element(*HomePage.proceedtocheckout).click()
        return list

    def getTopDeal(self):
        time.sleep(2)
        p = self.driver.window_handles
        self.driver.find_element(*HomePage.Top_Deal).click()
        time.sleep(2)
        chwd = self.driver.window_handles
        # HomePage.logN.getlogger().info("Windows Handlers Are"+chwd)
        for w in chwd:
            # switch focus to child window
            if w != p:
                self.driver.switch_to.window(w)

        time.sleep(1)
        self.driver.find_element(*HomePage.Top_Deal_Search).send_keys("Wheat")
        time.sleep(2)

        # self.driver.switch_to.window(p)
