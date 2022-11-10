# 파일 입출력 문제 

#실습문제 1
'''
보유한 주식이 목표가에 도달했을 때의 종목별 수익금과 수익률을 출력해주는 프로그램을 작성해보자.
mystock.csv 파일로부터 종목, 매입가, 수량, 목표가 정보를 가져온다.

수익금 = (목표가 - 매입가)*수량
수익률 = (목표가/매입가-1)*100

mystock.csv
종목, 매입가, 수량, 목표가
삼성전자,85000,10,90000
NAVER,380000,5,400000
'''

import csv

data = [["종목", "매입가", "수량", "목표가"],
        ["삼성전자", 85000, 10, 90000],
        ["NAVER", 380000, 5, 400000]
]

file = open("mystock.csv", "w", newline="", encoding="UTF-8-SIG")
writer = csv.writer(file)
for d in data :
    writer.writerow(d)
file.close()


def show_profit(raw) :
    name = raw[0]
    purchase_price = int(raw[1])
    amount = int(raw[2])
    target_price = int(raw[3])

    profit = (target_price - purchase_price)*amount
    profit_ratio = (target_price/purchase_price-1)*100

    print(f"{name} {profit} {profit_ratio:.2f}%")

file = open("mystock.csv", "r", encoding="UTF-8-SIG")
reader = list(csv.reader(file))

# print(f"종목 : {reader[1][0]} 수익금 : {(int(reader[1][3])-int(reader[1][1]))*int(reader[1][2])}원 수익률 : {(int(reader[1][3])/int(reader[1][1])-1)*100 :.2f}%")

for d in reader[1:] :
    show_profit(d)
file.close()