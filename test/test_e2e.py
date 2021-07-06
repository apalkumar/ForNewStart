import time
import pytest
from PageObjects.CartPage import CartPage
from PageObjects.HomePage import HomePage
from PageObjects.confirmPage import ConfirmPage
from TestData import HomePageData
from utility.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, getData):
        log = self.getlogger()
        log.info("Below are used for Logging")
        homePage = HomePage(self.driver)
        cartPage = CartPage(self.driver)
        confirmPage = ConfirmPage(self.driver)


        # list2 =s []
        # homePage.SearchProduct().send_keys("ber")
        homePage.SearchProduct().send_keys(getData)
        # homePage.SearchProduct().send_keys(getData["search1"])
        time.sleep(1)
        sCunt = homePage.count()
        # print(sCunt)
        log.info("Count is ==>"+str(sCunt))
        assert sCunt == 3
        homePage.proceed_checkout()
        time.sleep(2)
        cartPage.print_veggies()
        confirmPage.confirmOrder()

    # @pytest.fixture(params=[{"search1":"ber"}, {"search2":"Ser"}])
    @pytest.fixture(params=HomePageData.TestHomePageData.TestDataHomePage)
    def getData(self, request):
        return request.param
