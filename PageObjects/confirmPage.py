from selenium.webdriver.support.select import Select


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    def confirmOrder(self):
        # time.sleep(4)
        oselect = Select(self.driver.find_element_by_xpath("//select[@style='width: 200px;']"))
        oselect.select_by_value("India")

        # Select the Check box for Term and Agreement
        self.driver.find_element_by_xpath("//input[@type='checkbox']").click()

        # Click on Proceed Button
        self.driver.find_element_by_xpath("//button[text()='Proceed']").click()
        # self.driver.close()
