# 조건문 활용 실습

#실습문제 4
'''
프로그램 사용자로부터 국어, 수학, 영어 성적이 입력된다.
세 과목의 평균점수가 80점 이상이면 합격이다.
그런데 점수에 따라 합격 또는 불합격이 정해지는 프로그램에 오류가 발생했다.
80점 이상일 경우 불합격이 표시되도록 프로그램을 작성해보자.
(단, 0점에서 100점 사이의 숫자를 입력하지 않으면 "잘못 입력하였습니다."를 출력해보자)
'''

Korean = int(input("국어 >>> "))
Math = int(input("수학 >>> "))
English = int(input("영어 >>> "))
avg = (Korean + Math + English)/3



if  Korean < 0 or Korean > 100 or Math < 0 or Math > 100 or English < 0 or English > 100 :
    print("잘못 입력하였습니다.")
elif avg >= 80 :
    print("불합격")
else :
    print("합격")


# 다른 형태의 풀이 1
'''
if 0 <= Korean <= 100 and 0 <= Math <= 100 and 0 <= English <= 100 :
    if avg >= 80 :
        print("불합격")
    else :
        print("합격")
else :
    print("잘못 입력하였습니다.")
'''