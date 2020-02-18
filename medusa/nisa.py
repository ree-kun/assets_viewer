from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def open_sbi_page():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://site1.sbisec.co.jp/ETGate/')

    return driver

def login(driver):
    driver.find_element_by_xpath('//*[@id="user_input"]/input').send_keys('write your id here')
    time.sleep(0.4)
    driver.find_element_by_xpath('//*[@id="password_input"]/input').send_keys('write your password here')

    driver.find_element_by_xpath('//*[@id="SUBAREA01"]/form/div/div/div/p[2]/a/input').click()
    time.sleep(0.2)

def logout(driver):
    driver.find_element_by_xpath('//*[@id="logoutM"]/a').click()

def open_nisa(driver):
    driver.execute_script('var element=document.getElementById("link02_account_menu"); element.style.display="block";')
    driver.find_element_by_xpath('//*[@id="link02_account_menu"]/ul/li[3]/a').click()
    time.sleep(0.5)

def get_amount_on_nisa(driver):
    rows = driver.find_elements_by_xpath('//*[@id="fundBalanceDiv"]/table/tbody/tr')
    for row in rows[:-1]:
        tds = row.find_elements_by_css_selector('td')
        atag = tds[0].find_element_by_css_selector('a')
        print(atag.text)
        print(tds[6].text)
        atag.send_keys(Keys.COMMAND + Keys.RETURN)

    for i in range(len(rows[:-1])):
        driver.switch_to.window(driver.window_handles[i + 1])
        update_date = driver.find_element_by_xpath('//*[@id="MAINAREA02_780"]/div[2]/div[1]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[2]/div/div[3]').text
        print(update_date)


driver = open_sbi_page()
login(driver)
open_nisa(driver)
get_amount_on_nisa(driver)

time.sleep(5)

logout(driver)
driver.quit()
