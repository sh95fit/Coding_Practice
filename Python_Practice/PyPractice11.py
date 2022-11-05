# 함수 기초 활용 실습

#실습문제 2
'''
로또에 당첨되서 퇴사를 하고 싶었던 김로또는 로또 예상번호 추출 프로그램을 파이썬으로 작성하려고 한다.
다음 조건에 따라 김로또의 프로그램을 완성해보자.

1. 로또 번호 6개를 생성한다
2. 로또 번호는 1~45까지의 랜덤한 번호다.
3. 6개의 숫자 모두 달라야 한다.
4. getRandomNumber() 함수를 사용해서 구현한다. (random 모듈의 sample 함수는 사용하지 않는다.)
'''

import random

def getRandomNumber() :
    number = random.randint(1,45)
    return number


def LottoNum() :
    num = []
    while True :
        random_num = getRandomNumber()
        if random_num not in num :
            num.append(random_num)
        if len(num) == 6 : break
    print("추출된 로또 번호")
    num.sort()
    for i in num :
        print(i, end = ' ')

LottoNum()
