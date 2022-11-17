# 문자열 실습
'''
지도 어플리케이션에서 소요시간을 크롤링하였더니 문자열 데이터였다.
소요시간을 비교하기 위해 시간을 모두 분으로 바꾸려고 한다.
다음과 같이 시간이 입력되면 분으로 바꾸어주는 프로그램을 작성하자.
'''
# 풀이
'''
import re

print("시간 -> 분 환산 프로그램")

input = input("소요시간을 입력해주세요(양식: x시간 x분) >>> ")
print(f"입력한 시간 : {input}")

if '시간' not in input :
    input = re.findall(r'\d+', input)
    minute = input[0]
    print(f"분으로 환산된 결과값 : {minute}분")

elif '분' not in input  :
    input = re.findall(r'\d+', input)
    minute = int(input[0])*60
    print(f"분으로 환산된 결과값 : {minute}분")
else :
    input = re.findall(r'\d+', input)
    minute = int(input[0])*60 + int(input[1])
    print(f"분으로 환산된 결과값 : {minute}분")
'''

# 다른 풀이
time = input("시간을 입력하세요 >>> ")
# 1. 분만 있는 경우 ex> 30분
# 2. 시간만 있는 경우 ex> 2시간
# 3. 시간과 분이 있는 경우 ex> 1시간 30분

if time.find("시간") == -1 :
    # 분만 있는 경우
    result = int(time.split('분')[0])   # 분을 기준으로! 앞에 문자열을 자름 **기준 문자열 바로 뒷 부분도 자름(공백이 반영된다!!)
else :
    if time.find('분') == -1 :
        # 시간만 있는 경우
        result = int(time.split('시간')[0])*60
    else :
        hour = time.split('시간')
        result = int(hour[0])*60 + int(hour[1].split('분')[0])
print(result)