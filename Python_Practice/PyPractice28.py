# 파이썬 문제 풀이5

'''
문제
n개의 전화번호가 공백으로 구분된 문자열 A가 주어진다. 문자열 A에는 중복된 전화번호가 존재할 수 있다. 
추가로, 하나의 전화번호 B가 주어진다. 전화번호는 문자 ‘1’ ~ 문자 ‘9’로 이루어진 문자열이다. 
문자열 A에 포함된 전화번호 중에서 전화번호 B와 다르면서 B를 접두사로 갖는 전화번호의 개수를 출력하자. 
전화번호 T의 접두사는 T의 첫 번째 문자부터 한 개 이상의 연속된 문자로 구성된 부분 문자열을 의미한다. 
예를 들어, 전화번호 T=’1234’의 접두사는 전화번호 ‘1’, ‘12’, ‘123’, '1234'이다.

입력
첫 번째 줄에 문자열 A가 주어진다.

두 번째 줄에 전화번호 B가 주어진다.

출력
문자열 A에 포함된 전화번호 중에서 전화번호 B와 다르면서 B를 접두사로 갖는 전화번호의 개수를 출력한다.

제한
1 ≤ n ≤ 100,000
2 ≤ 문자열 A 길이 ≤ 1,000,000
2 ≤ 전화번호 길이 ≤ 10
전화번호는 문자 ‘1’ ~ 문자 ‘9’로 이루어진 문자열이다.

입력예제                                                          출력예제
12 121 123 1234 134 135 21 2134                          3
12


111 112 1111 121 13 21 22 23 24 31 119                 4
11

11 111 112 1111 121 13 21 22 23 24 31 119            0
1234
'''

A = input("문자열을 입력하세요 >>> ")
A = A.split()
B = input("접두사를 입력하세요 >>> ")

filtered_item = filter(lambda text : B in text and text != B, A)

print(len(list(filtered_item)))

'''
문제
알파벳 대소문자로 구성된 문자열 A가 주어진다. 
한 개 이상의 알파벳 대문자가 공백으로 구분된 문자 목록 B가 주어진다. 
문자 목록 B에는 중복된 대문자가 존재하지 않는다. 
문자 목록 B에 존재하는 모든 대문자 b에 대하여, 문자열 A에 존재하는 대문자 b를 대응하는 소문자로 치환한 문자열을 C라고 하자. 
입력으로 문자열 A와 문자 목록 B가 주어지면 문자열 C를 출력하자.

입력
첫 번째 줄에 문자열 A가 주어진다.

두 번째 줄에 문자 목록 B가 주어진다.

출력
첫 번째 줄에 문자열 C를 출력한다.

제한
3 ≤ 문자열 A 길이 ≤ 100,000
1 ≤ 문자 목록 B에 있는 대문자의 개수 ≤ 26
문자 목록 B에는 중복된 대문자가 존재하지 않는다.

입력예제             출력예제
ABabC                aBabC
A

ABabC                ababC
A B D
'''

A = input("문자열 A를 입력하시오 >>> ")
A = list(A)
print(A)
B = input("공백으로 구분된 문자열 B를 입력하시요 >>> ")

def upper(x) :
    return x.upper()

B = list(map(upper, B.split()))
print(B)

print(''.join(list(map(lambda data : data.lower() if data in B else data, A))))
