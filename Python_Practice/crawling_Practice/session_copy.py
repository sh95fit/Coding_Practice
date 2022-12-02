import requests
from selenium import webdriver
import login_info

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome("C:/chromedriver.exe", options=options)
#driver.get('https://rems.energy.or.kr/pub/view/login')

hdr = {'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}


def transfer_session() :

    session = requests.session()
    s = session.get('https://rems.energy.or.kr/pub/view/login', data = login_info.login_info, headers=hdr)
    s.raise_for_status()
    s.get('https://rems.energy.or.kr/pub/view/login')
    s.post('https://rems.energy.or.kr/pub/view/login/login_check.php', data = login_info.login_info)
    driver.get('https://rems.energy.or.kr/pub/view/login')
    for c in s.cookies :
        driver.add_cookie({'name' : c.name, 'value' : c.value, 'path' : c.path, 'expiry' : c.expires})
    driver.refresh()
    return