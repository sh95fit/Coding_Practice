# 반복문(For, While문) 활용 실습

#실습문제 2
'''
패스트게임즈에 인턴으로 근무하게 된 종현.
사수에게 과제로 게임 메뉴 만들기를 받았다.
과제 내용은 다음과 같았다.

- 과제 -
숫자1 입력 : "게임을 시작합니다" 출력
숫자2 입력 : "실시간 랭킹" 출력
숫자3 입력 : "게임을 종료합니다" 출력 후 프로그램 종료
(단, 3을 입력할 때까지 프로그램은 계속 실행된다.
1~3 외 다른 숫자를 입력하는 경우 "다시 입력해주세요"를 출력)
'''

while True :
    print("-----메뉴를 선택하세요-----")
    x = int(input("1. 게임시작   2. 랭킹보기   3. 게임종료 >>> "))
    if x == 1 : print("게임을 시작합니다!")
    elif x == 2 : print("실시간 랭킹 출력")
    elif x == 3 : 
        print("게임을 종료합니다.")
        break
    else : print("다시 입력해주시요")