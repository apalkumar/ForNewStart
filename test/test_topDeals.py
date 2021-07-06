from PageObjects.HomePage import HomePage
from utility.BaseClass import BaseClass


class TestTopDeal(BaseClass):
    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.getTopDeal()








