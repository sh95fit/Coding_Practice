# 파이썬 문제 풀이3

# 51.투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
investment = input("투자 중인 종목명을 입력하세요 >>> ")
if investment in warn_investment_list :
    print("투자 경고 종목입니다.")
else :
    print("투자 경고 종목이 아닙니다.")


# 52. 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
select_fruit = input("계절 이름을 입력하세요 >>> ")
if select_fruit in fruit.keys() :
    print("정답입니다.")
else : 
    print("오답입니다.")


# 53. 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
# >> a
string_input = input("문자 1개를 입력하세요 >>> ")
if string_input == string_input.lower() :       # 또는 string_input.islower() : 조건 활용
    string_input = string_input.upper()
else :
    string_input = string_input.lower()
print(string_input)


# 54. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
# 점수	        학점
# 81~100	A
# 61~80	        B
# 41~60	        C
# 21~40	        D
# 0~20	        E
# >> score: 83
score = int(input("점수를 입력하세요 >>> "))
if score > 80 and score <= 100 :
    print("A")
elif score > 60 and score <= 80 :
    print("B")
elif score > 40 and score <= 60 :
    print("C")
elif score > 20 and score <= 40 :
    print("D")
elif score > 0 and score <= 20 :
    print("F")

# 55. 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 
# 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
# 화명	환율
# 달러	1167
# 엔	1.096
# 유로	1268
# 위안	171
print("-----환율 계산기-----")
print("1. 달러  2. 엔  3. 유로  4. 위안")
select = float(input("환산할 단위의 번호 선택하세요. >>> "))
price = float(input("액수를 입력하세요 >>> "))
if select == 1 :
    print(price*1167,'원')
elif select == 2 :
    print(price*1.096,'원')
elif select == 3 :
    print(price*1268,'원')
elif select == 4 :
    print(price*171,'원')    
else :
    print("선택한 단위는 존재하지 않습니다.")


print("-----다른 방법-----")
rate = {"달러" : 1167, "엔" : 1.096, "유로" : 1268, "위안" : 171}
s = input("환율 : ")
n, currency = s.split()
print(float(n)*rate[currency], '원')

# 56. 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
num = []
num1 = int(input("첫 번째 숫자를 입력하세요 >>> "))
num.append(num1)
num2 = int(input("두 번째 숫자를 입력하세요 >>> "))
num.append(num2)
num3 = int(input("세 번째 숫자를 입력하세요 >>> "))
num.append(num3)
print(max(num))