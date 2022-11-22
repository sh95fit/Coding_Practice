import datetime
import csv
import os.path   #파일 존재 유무 확인용!
import time    # 딜레이 함수 사용
import requests
from bs4 import BeautifulSoup

'''
#WHILE 루프 안으로 이동

now = datetime.datetime.now()
nowDate = now.strftime("%Y%m%d")

csvname = "%s_발전데이터.csv"%(nowDate)
csvfile = open("./Python_Practice/"+csvname, 'a', newline="")
writer = csv.writer(csvfile)
if os.path.isfile(csvname) :
    title = ["설비용량","금일발전량","금일발전시간","전일발전량","전일발전시간","금월발전량","금월발전시간","금년발젼랑","금년발전시간","누적발전량","CO2저감량","식수효과"]
    writer.writerow(title)
'''

#gsrems.co.kr 로그인 세션 구현
id = input("id >>> ")
password = input("password >>> ")
plant_id = input("추출할 발전소 번호 입력 >>> ")

login_info = {'id':id, 'password':password}

session = requests.session()

url_login = "http://gsrems.co.kr/auth/login"
res = session.post(url_login, data = login_info)
res.raise_for_status()

# 해당 발전소 페이지 이동 세션
webpage = "http://gsrems.co.kr/monitoring/plant/"+plant_id
res = session.get(webpage)
res.raise_for_status()
print(res)
soup = BeautifulSoup(res.text, 'html.parser')

date_check = 0

while date_check != "2000" :
#설비용량, 금일발전량, 금일발전시간, 전일발전량, 전일발전시간, 금월발전량, 금월발전시간, 금년발전량, 금년발전시간, 누적발전량, CO2저감량, 식수효과
    now = datetime.datetime.now()
    nowDate = now.strftime("%Y%m%d")
    date_check = now.strftime("%H%m")

    csvname = "%s_발전데이터.csv"%(nowDate)
    csvfile = open("./Python_Practice/"+csvname, 'a', newline="")
    writer = csv.writer(csvfile)
    if os.path.isfile(csvname) :
        title = ["설비용량","금일발전량","금일발전시간","전일발전량","전일발전시간","금월발전량","금월발전시간","금년발젼랑","금년발전시간","누적발전량","CO2저감량","식수효과"]
        writer.writerow(title)

    raw_data = []
    table = soup.find('table', class_="table custom-table mb-0").find_all('strong')
    for data in table :
        raw_data.append(data.getText())
    writer.writerow(raw_data)
    csvfile.close()
    print("발전데이터가 정상적으로 저장되었습니다.")
    #table custom-table mb-0 : 발전현황 우측 테이블
    time.sleep(60)

'''
#select문 test
#table = soup.select("body > div.wrap > div.content.container > div.row > div:nth-child(1) > section > div > div > div:nth-child(2) > table")

#설비용량
capa = soup.select_one("body > div.wrap > div.content.container > div.row > div:nth-child(1) > section > div > div > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(2) > span:nth-child(1) > strong").getText()

#금일발전량
tpg = soup.select_one("body > div.wrap > div.content.container > div.row > div:nth-child(1) > section > div > div > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(2) > span:nth-child(1) > strong").getText()
'''