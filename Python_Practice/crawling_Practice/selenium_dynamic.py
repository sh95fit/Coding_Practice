from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome("C:/chromedriver.exe", options=options)

driver.implicitly_wait(3)

driver.get('https://rems.energy.or.kr/admin/monitor/view/monitorCmb')

print(driver.title)

sleep(5)

data = driver.find_element(By.XPATH, '//*[@id="GelecQty"]').text

print(data)

sleep(2)

driver.quit()