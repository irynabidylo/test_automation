from Data_Driven_Testing import Excel_utils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\Program Files\Drivers_browsers\chromedriver.exe")
driver.get("https://www.italki.com/")

driver.maximize_window()
driver.implicitly_wait(2) #waits for 2 seconds for a page to open

path = "C://Users/Andrey/PycharmProjects/Seleniumwithpython/Excel_files_for_Selenium/Login1.xlsx"


rows = Excel_utils.get_row_count(path,"Лист1")

main_page = driver.find_element_by_xpath("//*[@id='__next']/div/header/nav/div[1]/a[4]").click()

for r in range(2, rows+1): #starts with 2, because 1st row is a header


    email = Excel_utils.read_data(path, "Лист1", r, 1) #1 - as username is in column 1
    password = Excel_utils.read_data(path, "Лист1", r, 2) #2 - as password is stored in column 2
    driver.find_element_by_id("username_id").send_keys(email)
    driver.find_element_by_id("password_id").send_keys(password)

    driver.find_element_by_id("login").click()
    driver.implicitly_wait(5) #waits for 5 seconds for a page to open

    #to check that the login was succesful - capture the title of the page:
    if driver.title == "italki: Learn a language online | italki":
        print("Test Passed")
        Excel_utils.write_data(path, "Лист1", r, 3, "Test Passed") #3 - REsults are in the column 3 in the file

        # mouse hover to element to exit
        exit = driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div/a[4]")
        action = ActionChains(driver)
        action.move_to_element(exit).click().perform()
        #scrolls down the page till the button "Exit" is visible
        exit_click = driver.find_element_by_xpath("//*[@id='header_container']/div[1]/div/div/div/ul/li[13]/div/span")
        driver.execute_script("arguments[0].scrollIntoView();", exit_click)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='header_container']/div[1]/div/div/div/ul/li[13]/div/div").click()

        main_page.click()
    else:
        print("Test Failed")
        Excel_utils.write_data(path, "Лист1", r, 3, "Test Failed")


#driver.quit()       #closes all the tabs/ the whole window
