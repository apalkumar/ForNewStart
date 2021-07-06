import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    veggies = (By.XPATH, "//p[@class='product-name']")
    amounts = (By.XPATH, "//tr/td[5]/p")
    Total_Amount = (By.XPATH, "//span[@class='totAmt']")
    pCode = (By.XPATH, "//input[@placeholder='Enter promo code']")
    Apply = (By.XPATH, "//button[text()='Apply']")

    def __init__(self, driver):
        self.driver = driver

    def print_veggies(self):
        list2 = []
        strVeggies = self.driver.find_elements(*CartPage.veggies)
        list2.clear()
        for veg in strVeggies:
            list2.append(veg.text)

        del list2[3:6]
        print(list2)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
        self.driver.find_element_by_xpath("//button[text()='Apply']").click()
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Code applied ..!']")))
        flag_dislayed1 = self.driver.find_element_by_xpath("//span[text()='Code applied ..!']").is_displayed()
        print(flag_dislayed1)
        assert flag_dislayed1
        self.driver.find_element_by_xpath("//button[text()='Place Order']").click()
