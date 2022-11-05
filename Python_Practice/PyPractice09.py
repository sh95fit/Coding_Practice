# 반복문(For, While문) 활용 실습

#실습문제 3
'''
성민은 패스트대학교에서 Lily라는 이름의 교환학생과 친해지게 되었다.
영어를 잘하지 못했던 성민은, Lily에게 한국어를 가르쳐 주기 위해 한국어 연습 프로그램을 만들게 되었다.

- Learning Korean -
1. 연습할 한국어가 담긴 리스트를 만든다.
2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다.
3. 프로그램 사용자는 단어를 그대로 입력하고
4. 맞추면 다음 단어를 가져온다. 틀리면 프로그램 종료.
'''
korean = ['사랑해', '고마워', '행복해']

'''
print("Let's learn Korean")
for i in korean :
    print("문제 : %s"%(i))
    x = input("정답 >>> ")
    if i != x : 
        print("실패!!")
        break
'''

# 프로그램 업그레이드
# 전체 문제 개수, 맞힌 문제 개수, 틀린 문제 개수 출력
wrong_score = 0

print("Let's learn Korean")

for i in korean :
    print("문제 : %s"%(i))
    x = input("정답 >>> ")
    if i != x : 
        wrong_score += 1

print("전체 문제 개수 : %d"%len(korean))
print("맞춘 문제 개수 : %d"%(len(korean)-wrong_score))
print("틀린 문제 개수 : %d"%wrong_score)