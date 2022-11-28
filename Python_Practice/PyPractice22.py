#정규표현식 실습문제 2
'''
현지는 자사상품이벤트를 위해 고객들로부터 이메일을 입력 받는다.
고객들이 이메일 양식을 올바르게 입력하는지 검사하는 정규표현식을 작성해보자.

1. 이메일은 ID 파트와 host 파트가 있다. (ID @ host)
2. ID 파트는 영문 대소문자, 숫자, 특수문자(-_)가 들어갈 수 있다.
3. host 파트는 영문 대소문자, 숫자, 특수문자(-)
4. host 파트는 2개 이상의 도메인으로 구성될 수 있다.
'''

import re

datas = [
    'startcoding@maver.com',
    'start-coding@maver.com',
    'start_coding@maver.co.kr',
    'startcoding@k-mail.com',
    '@maver.com',
    'startcoding?@k-mail.com',
    'startcoding@k-mail',
    'startcoding@maver'
]


'''
regex = '(([\w|\-]){1,})@(([\w|\-]){1,}\.{1,}.*)'

for data in datas :
    matchObj = re.match(regex, data)
    result = (lambda x : True if x != None else False)(matchObj)
    print(f"{data} : {result}")
'''


# 컴파일을 미리 해놓는 방법  (컴파일은 자원은 많이 소진하므로 while 루프 안애 들어가면 효율이 좋지 않음!)
regex = re.compile('^[\w-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+$')              # [a-zA-Z0-9_] == \w 로 줄여쓸 수 있다!  즉 \w 는 대소문자, 숫자, 언더바(_)를 포함하는 값들을 의미!

for data in datas : 
#    matchObj = re.match(regex, data)
#   컴파일을 미리 한 경우 match
    matchObj = regex.match(data)
    result = (lambda x : True if x != None else False)(matchObj)
    print(f"{data} : {result}")