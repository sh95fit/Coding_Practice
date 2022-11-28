#정규표현식 실습 문제
'''
민수는 날짜 형식을 검사하는 정규표현식을 만드는 업무를 받았다.
업무 내용은 다음과 같다.
Jason 팀장 : "YYYY/MM/DD"형식으로 표현된 날짜를 검사해주세요"

1. 연도는 4자리 숫자로 제한한다. (1000~9999)
2. 월은 1월~12월, 일은 1일~31일까지 가능하다
'''
import re

datas = [
    '2022/08/08',
    '1000/01/01',
    '9999/12/31',
    '900/02/02',
    '12000/10/16',
    '2021/13/01',
    '2023/2/02',
    '2024/06/3',
    '2023/06/35'
]

regex = '^(\d{4})\/(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[0-1])$'

for data in datas :
    matchObj = re.match(regex, data)
    result = (lambda x : True if x != None else False)(matchObj)
    print(f"{data} : {result}")


'''
for data in datas :
    if re.findall('^(\d{4})\/(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[0-1])$', data) != [] :
        print(data + " True")
    else :
        print(data + " False")
'''

'''
for data in datas :
    if re.findall('^(\d{4})\/(\d{2})\/(\d{2})$', data) != [] :
        if int(re.findall('^(\d{4})\/(\d{2})\/(\d{2})$', data)[0][1]) <= 12 and int(re.findall('^(\d{4})\/(\d{2})\/(\d{2})$', data)[0][2]) <= 31 :
            print(data + " True")
        else :
            print(data + " False")
    else :
        print(data + " False")
'''
