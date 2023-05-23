from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_negative():

    # create a driver
    driver = webdriver.Chrome()

    # open login page # later we will do a fixture here
    driver.get("https://github.com/login")

    # enter wrong/correct email
    login_fld = driver.find_element(By.ID, "login_field")
    login_fld.send_keys("some _incorectemail@gmail.com")
    # time.sleep(3) # 3 sec, NEVER USE IN PROD SERVER!!

    id = "login_field"

    # enter wrong password
    pass_fld = driver.find_element(By.ID, "password")
    pass_fld.send_keys("dsgsegd")
    # time.sleep(3) # 3 sec, NEVER USE IN PROD SERVER!!

    password = "password"
    
    # click signin button
    signin_btn = driver.find_element(By.NAME, "commit")
    signin_btn.click()

    name = "commit"
    time.sleep(3)
    
    # check error message

    driver.quit()
