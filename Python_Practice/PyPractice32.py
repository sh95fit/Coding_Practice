# 파이썬 문제 풀이 8
'''
1.
16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
영일이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.

A, B, C, D, E, F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
(단, A ~ F 까지만 입력된다.)

입력예시
B

출력예시
B * 1 = B
B * 2 = 16
B * 3 = 21
B * 4 = 2C
B * 5 = 37
B * 6 = 42
B * 7 = 4D
B * 8 = 58
B * 9 = 63
B * A = 6E
B * B = 79
B * C = 84
B * D = 8F
B * E = 9A
B * F = A5
'''
# dan = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
#        'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
# convert_dan = {n:c for c,n in dan.items()}
# result = ''
# n = input("몇 단을 출력하시겠습니까? >>> ")
# for i in range(1,16) :
#     num = dan[n]
    
#     num_1 = (num*i)//16
#     num_2 = (num*i)%16

#     if num_1 >= 10 :
#         num_1 = convert_dan.get(num_1)
#     if num_2 >= 10 :
#         num_2 = convert_dan.get(num_2) 
#     if i >= 10 :
#         i = convert_dan.get(i)
#     if str(num_1) == '0' :
#         result = str(num_2)
#     else :
#         result = str(num_1) + str(num_2)

#     print(f"{n} * {i} = {result}")   


# 다른 풀이
n = int(input(), 16)
for i in range(1, 16) :
    print("%X x %X = %X"%(n, i, (n*i)))


'''
2.
1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
나올 수 있는 모든 경우를 출력해보자.

예시
...
for i in range(1, n+1) :
  for j in range(1, m+1) :
    print(i, j)
...

참고
위 코드는
바깥쪽의 i 값이 1부터 n까지 순서대로 바뀌는 각각의 동안에
안쪽의 j 값이 다시 1부터 m까지 변하며 출력되는 코드이다.

조건선택 실행구조 안에 다른 조건선택 실행구조를 넣어 처리할 수 있는 것과 마찬가지로
반복 실행구조 안에 다른 반복 실행구조를 넣어 처리할 수 있다.

원하는 형태로 실행 구조를 결합하거나 중첩시킬 수 있다.

입력예시
2 3

출력예시
1 1
1 2
1 3
2 1
2 2
2 3
'''

# n = input().split(' ')
# for i in range(1,int(n[0])+1) :
#     for j in range(1,int(n[1])+1) :
#         print(i,j)

# 다른 풀이
n, m = map(int, input().split())
for i in range(1, n+1) :
    for j in range(1, m+1) :
        print(i,j)



'''
3.
숫자를 한글로 변환하기
12345->일만이천삼백사십오
'''
# num = {'1' : '일', '2' : '이', '3' : '삼', '4' : '사', '5' : '오', '6' : '육', '7' : '칠', '8' : '팔', '9' : '구', '0' : ''}
# unit_1 = ['', '십', '백', '천']
# unit_2 = ['', '만', '억', '조']

# n = input()
# string = ''
# if(len(n) <= 4) :
#     for i in range(len(n)) :
#         string += num[n[i]] + unit_1[len(n)-(i+1)] 
# elif(len(n) <= 8 and len(n) > 4) :
#     for i in range(len(n)-4) :
#         string += num[n[i]] + unit_1[len(n) % 4-(i+1)]
#     if len(n)-4 >= 1 or len(n)-4 <= 4 :
#         string += unit_2[1]
#     for i in range(len(n)-4, len(n)):
#         string += num[n[i]] + unit_1[len(n)-(i+1)]
# elif(len(n) <= 12 and len(n) > 8) :
#     for i in range(len(n)-8) :
#         string += num[n[i]] + unit_1[len(n) % 4-(i+1)]
#     if len(n)-8 >= 1 or len(n)-8 <= 4:
#         string += unit_2[2]
#     for i in range(len(n)-8, len(n)-4):
#         string += num[n[i]] + unit_1[len(n) % 4-(i%4+1)]
#     if len(n)-4 >= 1 or len(n)-4 <= 4:
#         string += unit_2[1]
#     for i in range(len(n)-4, len(n)):
#         string += num[n[i]] + unit_1[len(n)-(i+1)]
# elif(len(n) <= 16 and len(n) > 12):
#     for i in range(len(n)-12):
#         string += num[n[i]] + unit_1[len(n) % 4-(i+1)]
#     if len(n)-12 >= 1 or len(n)-4 <= 12:
#         string += unit_2[3]
#     for i in range(len(n)-12, len(n)-8):
#         string += num[n[i]] + unit_1[len(n) % 4-(i%4+1)]
#     if len(n)-8 >= 1 or len(n)-8 <= 4:
#         string += unit_2[2]
#     for i in range(len(n)-8, len(n)-4):
#         string += num[n[i]] + unit_1[len(n) % 4-(i%4+1)]
#     if len(n)-4 >= 1 or len(n)-4 <= 4:
#         string += unit_2[1]
#     for i in range(len(n)-4, len(n)):
#         string += num[n[i]] + unit_1[len(n)-(i+1)]
# print(string)


# 다른 풀이
n = int(input())
numbers = ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
a = ["","십","백","천"]
result = []
i = 0
while n>0 :
    n, r = divmod(n, 10)
    if r > 0 :
        result.append(numbers[r-1]+a[i])
    i += 1
print(''.join(result[::-1]))

'''
4. 
친구들과 함께 3 6 9 게임을 하던 영일이는 잦은 실수 때문에 계속해서 벌칙을 받게 되었다.
3 6 9 게임의 왕이 되기 위한 369 마스터 프로그램을 작성해 보자.

** 3 6 9 게임은?
여러 사람이 순서를 정한 후, 순서대로 수를 부르는 게임이다.
만약 3, 6, 9 가 들어간 수를 자신이 불러야 하는 상황이라면, 수를 부르는 대신 "박수(X)" 를 쳐야 한다.
33과 같이 3,6,9가 두 번 들어간 수 일때, "짝짝"과 같이 박수를 두 번 치는 형태도 있다. 
'''
# n = int(input())
# for i in range(n) :
#     if str(i).count('3') != 0 or str(i).count('6') != 0 or str(i).count('9'):
#         print("짝"*(str(i).count('3')+str(i).count('6')+str(i).count('9')))
#     else : 
#         print(i)


# 다른 풀이
n = int(input())

for i in range(1, n+1) :
    s = str(i)
    cnt = 0
    for x in s :
        if x == '3' or x == '6' or x == '9' :
            cnt += 1
        if cnt == 0 :
            print(i, end = ' ')
        else :
            print('짝'*cnt, end = ' ')
print("\n")

'''
5.
문제
우리나라 고유의 윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모를 결정한다. 네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 중 어떤 것인지를 결정하는 프로그램을 작성하라.

입력
첫째 줄부터 셋째 줄까지 각 줄에 각각 한 번 던진 윷짝들의 상태를 나타내는 네 개의 정수(0 또는 1)가  빈칸을 사이에 두고 주어진다.

출력
첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를  도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력한다.
'''

# result = {0 : 'E', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D'}

# f_time = sum(map(int, input("첫 번째 시도 : ").split(' ')))
# s_time = sum(map(int, input("두 번째 시도 : ").split(' ')))
# t_time = sum(map(int, input("세 번째 시도 : ").split(' ')))
# print(result[int(f_time)])
# print(result[int(s_time)])
# print(result[int(t_time)])


# 또 다른 풀이
for i in range(3) :
    a = list(map(int, input().split()))
    if a.count(0) == 1 :
        print('A')
    elif a.count(0) == 2 :
        print('B')
    elif a.count(0) == 3:
        print('C')
    elif a.count(0) == 4:
        print('D')
    elif a.count(0) == 0:
        print('E')
