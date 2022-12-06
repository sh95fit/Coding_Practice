# 파이썬 문제 풀이

'''
1. letters = 'python'
>> p t
'''

letters = 'python'
for i in range(len(letters)) :
    if i == 0 or i == 2 :
        print(letters[i], end=' ')


print("\n")
'''
2. license_plate = "24가 2210"
>> 2210
'''

license_plate = "24가 2210"
print(license_plate.split(' ')[1])


print("\n")
'''
3. string = "홀짝홀짝홀짝"
>> 홀홀홀
'''

string = "홀짝홀짝홀짝"
for i in string :
    if i == '홀' :
        print(i, end='')


print("\n")
'''
4. string = "PYTHON"
>> NOHTYP
'''
string = "PYTHON"
print("".join(reversed(string)))


print("\n")
'''
5. phone_number = "010-1111-2222"
>> 010 1111 2222
'''

phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))


print("\n")
'''
6. 화면에 '-'를 80개 출력하세요.
'''
for i in range(80):
    print("-", end="")


print("\n")
'''
7. t1 = 'python'
   t2 = 'java'

>> python java python java python java python java
'''
t1 = 'python'
t2 = 'java'

for i in range(4) :
    print(f"{t1} {t2}", end=" ")


print("\n")
'''
8. name1 = "김민수" 
   age1 = 10
   name2 = "이철희"
   age2 = 13

>> 이름: 김민수 나이: 10
>> 이름: 이철희 나이: 13
'''
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

person = {name1:age1, name2:age2}

for key, value in person.items() :
    print(f"이름 : {key} 나이 : {value}")


print("\n")
'''
9. 다음과 같은 문자열에서 '2020/03'만 출력하세요.
   분기 = "2020/03(E) (IFRS연결)"
'''
quarter = "2020/03(E) (IFRS연결)"

import re
print(re.findall("\d{4}\/\d{2}",quarter)[0])


print("\n")
'''
10. data = "   삼성전자    " 좌우공백 제거하세요
'''
data = "   삼성전자    "
print(data)
print(data.strip())


print("\n")
'''
11. 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
     ticker = "btc_krw"
'''
ticker = "btc_krw"
print(ticker.upper())


print("\n")
'''
12. 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
'''
string = 'hello'
print(string.capitalize())


print("\n")
'''
13. 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
     file_name = "보고서.xlsx"
'''
file_name = "보고서.xlsx"
if file_name.endswith('.xls') == True or file_name.endswith('.xlsx') == True :
    print('정상적인 확장자(.xlsx, .xls)를 사용하였습니다.')


print("\n")
'''
14. 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
     file_name = "2020_보고서.xlsx"
'''
file_name = "2020_보고서.xlsx"
if file_name.startswith("2020") == True :
    print('2020년도 자료입니다.')


print("\n")
'''
15. 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
     a = "hello world"
'''
a = "hello world"
a = a.split(" ")
print(a)


print("\n")
'''
16. 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
     ticker = "btc_krw"
'''
ticker = "btc_krw"
ticker = ticker.split("_")
print(ticker)


print("\n")
'''
movie = ["닥터 스트레인지", "스플릿", "럭키"]

17. movie 리스트에 "배트맨을" 추가하라.
18. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
19. 리스트에서 '럭키'를 삭제하라.
20. 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
'''
movie = ["닥터 스트레인지", "스플릿", "럭키"]

movie.append('배트맨')
print(movie)

movie.insert(1, '슈퍼맨')
print(movie)

movie.remove("럭키")
print(movie)

del movie[2:]
print(movie)


print("\n")
'''
21. 날짜 정보를 제외하고 가격 정보만을 출력하라.
     price = ['20180728', 100, 130, 140, 150, 160, 170]
>> [100, 130, 140, 150, 160, 170]
'''
price = ['20180728', 100, 130, 140, 150, 160, 170]
result = []
for i in price :
    if type(i) is int :
        result.append(i)
print(result)


print("\n")
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
22. 슬라이싱을 사용해서 홀수만 출력하라.
>> [1, 3, 5, 7, 9]
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])


print("\n")
'''
23. 슬라이싱을 사용해서 짝수만 출력하라.
>> [2, 4, 6, 8, 10]
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])


print("\n")
'''
24. 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
>> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::-1])


print("\n")
'''
25. interest = ['삼성전자', 'LG전자', 'Naver']
>> 삼성전자 Naver
'''
interest = ['삼성전자', 'LG전자', 'Naver']
print(' '.join(interest[::2]))


print("\n")
'''
26. interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
>> 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
>> 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
>> 삼성전자
   LG전자
   Naver
   SK하이닉스
   미래에셋대우
'''
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest[::]))
print('/'.join(interest[::]))
print('\n'.join(interest[::]))


print("\n")
'''
27. string = "삼성전자/LG전자/Naver"
>> ['삼성전자', 'LG전자', 'Naver']
'''
string = "삼성전자/LG전자/Naver"
print(string.split("/"))


print("\n")
'''
28. data = [2, 4, 3, 1, 5, 10, 9]
>> [1, 2, 3, 4, 5, 9, 10]
'''
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))


print("\n")
'''
29. t = ('a', 'b', 'c') 변수 t 가  ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
'''
t = ('a', 'b', 'c')
t = list(t)
t[0] = 'A'
t = tuple(t)
print(t)


print("\n")
'''
30. interest = ('삼성전자', 'LG전자', 'SK Hynix')를 리스트로 변환하라.
'''
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)


print("\n")
'''
31. interest = ['삼성전자', 'LG전자', 'SK Hynix']를 튜플로 변경하라.
'''
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest)


print("\n")
'''
32. 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
'''
num = []
for i in range(1,100) :
    if i%2 == 0 :
        num.append(i)
num = tuple(num)
print(num)
