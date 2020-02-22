from selenium import webdriver
import time

def open_401k_page():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://www.benefit401k.com/customer/')

    return driver

def login(driver):
    driver.find_element_by_id('txtUserID').send_keys('write your id here')
    time.sleep(0.4)
    driver.find_element_by_id('txtPassword').send_keys('write your password here')

    driver.find_element_by_id('btnLogin').click()
    time.sleep(0.5)

def logout(driver):
    driver.find_element_by_id('D_Header1_btnLogout').click()

def get_amount(driver):
    amount = driver.find_element_by_id('D_Header1_lblKojinBalanceAssets').text
    print(amount)


driver = open_401k_page()
login(driver)
get_amount(driver)

time.sleep(5)

logout(driver)
driver.quit()
