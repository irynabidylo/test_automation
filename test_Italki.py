from selenium import webdriver
import unittest

class ItalkiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers_browsers\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls): 
        cls.driver.quit()
        print("Test completed")

    def test_homepage_title_verification(self):
        self.driver.get("https://www.italki.com")
        self.assertEqual("italki: Learn a language online", self.driver.title, "Titles don't match")
        #"Titles don't match" - message which will be shown if test fails

    def test_login(self):
        self.driver.get("https://www.italki.com/signin?hl=ru")
        self.driver.find_element_by_id("signinForm_email").send_keys("test_email@gmail.com")
        self.driver.find_element_by_id("signinForm_password").send_keys("123456789aB")
        self.driver.find_element_by_class_name("ant-btn ant-btn-secondary ant-btn-block").click()
        self.assertEqual("Панель управления | italki", self.driver.title, "Titles don't match")
        #"Titles don't match" - message which will be shown if test fails

if __name__ == '__main__':
    unittest.main()
