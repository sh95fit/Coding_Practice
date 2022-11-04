# 리스트 자료형 활용 실습

#실습문제 2
'''
턱걸이 평균 측정 프로그램을 만들어보자.
먼저, 턱걸이 횟수를 저장할 빈 리스트를 만든다.
그리고 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장한다.
리스트에 저장된 데이터의 평균을 구해 출력한다.
'''
count = [] # 빈 리스트 생성
sum = 0
avg = 0

for i in range(7) :
    count.append(int(input(str(i+1) + "일차 턱걸이 횟수 >>> ")))

for i in count[:]:
    sum += i
avg = sum/len(count)
print("평균 = %d" % (avg))

#count.append(int(input("1일차 턱걸이 횟수 >>> ")))
#count.append(int(input("2일차 턱걸이 횟수 >>> ")))
#count.append(int(input("3일차 턱걸이 횟수 >>> ")))
#count.append(int(input("4일차 턱걸이 횟수 >>> ")))
#count.append(int(input("5일차 턱걸이 횟수 >>> ")))
#count.append(int(input("6일차 턱걸이 횟수 >>> ")))
#count.append(int(input("7일차 턱걸이 횟수 >>> ")))



# 다른 방안
'''
count = []

a = int(input("1일차 턱걸이 횟수 >>> "))
count.append(a)
a = int(input("2일차 턱걸이 횟수 >>> "))
count.append(a)
a = int(input("3일차 턱걸이 횟수 >>> "))
count.append(a)
a = int(input("4일차 턱걸이 횟수 >>> "))
count.append(a)
a = int(input("5일차 턱걸이 횟수 >>> "))
count.append(a)
a = int(input("6일차 턱걸이 횟수 >>> "))
count.append(a)
a = int(input("7일차 턱걸이 횟수 >>> "))
count.append(a)

total = count[0] + count[1] + count[2] + count[3] + count[4] + count[5] + count[6]
avg = total/7

print(int(avg))
'''