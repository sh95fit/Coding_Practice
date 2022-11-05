# 함수 기초 활용 실습

#실습문제 1
'''
다음은 세 개의 정수를 인자로 받아 합계와 평균을 출력해주는 함수이다.
함수를 정의해보자.
'''

def printSumAvg(x,y,z):
    print(f"합계 : {x + y + z} 평균 : {(x + y + z)/3}")

printSumAvg(10,20,30)


'''
Tip : 문자열 포맷팅
문자열 시작전
f"문자열 {변수} 문자열 {변수}"    / 변수가 들어갈 자리를 {} : 중괄호로 처리!
'''