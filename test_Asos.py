from selenium import webdriver
import pytest
from selenium.webdriver.support.select import Select
import time

class TestAsos():

    @pytest.fixture #will execute before each test method
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers_browsers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://my.asos.com/identity/register?lang=en-GB&store=COM&country=GB&keyStoreDataversion=hnm9sjt-28&returnUrl=https%3A%2F%2Fwww.asos.com%2F%3F&_ga=2.186066794.276499641.1629168403-399707905.1609706787")
        self.driver.implicitly_wait(5)
        yield
        self.driver.close()

    def test_pagetitle(self,setup):
        assert self.driver.title == "ASOS | Join ASOS"

    def test_registration(self,setup):

        self.driver.find_element_by_name("Email").send_keys("john_doe_07@gmail.com")
        self.driver.find_element_by_name("FirstName").send_keys("John")
        self.driver.find_element_by_name("LastName").send_keys("Doe")
        self.driver.find_element_by_name("Password").send_keys("0123456789")

        #scroll till element is visible on page:
        scroll_birth_date = self.driver.find_element_by_name("BirthDay")
        scroll_birth_date.location_once_scrolled_into_view

        #selects the day of birth by visible text (5)
        bith_day = Select(self.driver.find_element_by_name("BirthDay"))
        bith_day.select_by_visible_text("5")

        #selects the month of birth by index (April)
        birth_month = Select(self.driver.find_element_by_name("BirthMonth"))
        birth_month.select_by_index(4)

        #selects the year of birth by value (1990)
        birth_year = Select(self.driver.find_element_by_name("BirthYear"))
        birth_year.select_by_value("1990")


        womenswear = self.driver.find_element_by_id("femaleLabel")
        womenswear.click()

        #contact preferences
        self.driver.find_element_by_id("promosLabel").click() #discounts_and_sales
        self.driver.find_element_by_id("newness").click() #new_stuff

        self.driver.find_element_by_id("register").click()
        time.sleep(6)
        assert self.driver.title == "ASOS | Online shopping for the Latest Clothes & Fashion"
