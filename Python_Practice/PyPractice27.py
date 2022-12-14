# 파이썬 문제 풀이4

'''
57. 3개의 시간조절용 버튼 A B C가 달린 전자레인지가 있다. 각 버튼마다 일정한 시간이 지정되어 있어 해당 버튼을 한번 누를 때마다 그 시간이 동작시간에 더해진다. 버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초이다.

냉동음식마다 전자레인지로 요리해야할 시간 T가 초단위로 표시되어 있다. 우리는 A, B, C 3개의 버튼을 적절히 눌러서 그 시간의 합이 정확히 T초가 되도록 해야 한다. 단 버튼 A, B, C를 누른 횟수의 합은 항상 최소가 되어야 한다. 이것을 최소버튼 조작이라고 한다. 

만일 요리시간이 100초라고 하면(T=100) B를 1번, C는 4번 누르면 된다. 이와 다르게 C를 10번 눌러도 100초가 되지만 이 경우 10번은 최소 횟수가 아니기 때문이 답이 될 수 없다. 이 경우 B 1번, C 4번, 총 5번이 최소버튼 조작이다. 그리고 T=234와 같이 3개의 버튼으로 시간을 정확히 맞출 수 없는 경우도 있다. 

여러분은 주어진 요리시간 T초를 맞추기 위한 최소버튼 조작 방법을 구하는 프로그램을 작성해야 한다. 


입력예시               출력예시
100              ->    0 1 4
189              ->    -1
'''
button = {'A' : 5*60, 'B' : 1*60, 'C' : 10}
count = 0
count_A = 0
count_B = 0
count_C = 0

time = input("요리 시간 입력(T) >>> ")

if int(time)%10 != 0 :
    print(-1)
else :
    while time != 0 :
        if int(time)//button['A'] >= 1 :
            count += int(time)//button['A']
            count_A = int(time)//button['A']
            time = int(time)%button['A']
        elif int(time)//button['B'] >= 1 :
            count += int(time)//button['B']
            count_B = int(time)//button['B']
            time = int(time)%button['B']
        else :
            count += int(time)//button['C']
            count_C = int(time)//button['C']
            time = int(time)%button['C']
    print(f"최소 조작 횟수 : {count} / A버튼 조작 횟수 : {count_A} / B버튼 조작 횟수 : {count_B} / C버튼 조작 횟수 : {count_C}")


'''
58. 상근이는 매일 아침 알람을 듣고 일어난다. 알람을 듣고 바로 일어나면 다행이겠지만, 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.

상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.

이런 상근이를 불쌍하게 보던, 창영이는 자신이 사용하는 방법을 추천해 주었다.

바로 "45분 일찍 알람 설정하기"이다.

이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.

현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.

입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

입력예시    출력예시
10 10       9 25
0 30         23 45
23 40       22 55
'''
clock = input("알람 시각을 입력하세요 >>> ")
hour, minute = clock.split()
if int(minute)-45 >= 0 :
    print(f"고쳐야할 시간 : {hour} {int(minute)-45}")
else :
    if int(hour)-1 >= 0 :
        print(f"고쳐야할 시간 : {int(hour)-1} {int(minute)+15}")
    else :
        print(f"고쳐야할 시간 : {23} {int(minute)+15}")

'''
59.그릇을 바닥에 놓았을 때 그 높이는 10cm 이다. 그런데 두 개의 그릇을 같은 방향으로 포개면 그 높이는 5cm만 증가된다. 만일 그릇이 서로 반대방향으로 쌓이면 높이는 그릇만큼, 즉 10cm 늘어난다. 그릇을 괄호 기호로 나타내어 설명해보자. 편의상 그릇이 쌓여지는 방향은 왼쪽에서 오른쪽이라고 가정한다. 그림에서 ‘(’은 그릇이 바닥에 바로 놓인 상태를 나타내며, ‘)’은 그릇이 거꾸로 놓인 상태를 나타낸다.

만일 그릇이 포개진 모양이 ((((와 같다면 전체의 높이는 25cm가 된다. 왜냐하면 처음 바닥에 있는 그릇의 높이가 10cm이고 이후 같은 방향으로 3개의 그릇이 포개져 있으므로 늘어난 높이는 5+5+5=15 이기 때문이다. ()()와 같은 경우라면 그 높이는 10*4=40cm가 된다.

여러분은 입력에 주어진 모양대로 그릇을 쌓을 때 최종의 전체 그릇 높이를 계산해서 출력해야 한다. 즉 처음 입력으로 주어진 각 그릇의 방향은 바꿀 수 없다. 

입력
첫 줄에는 괄호문자로만 이루어진 문자열이 주어진다. 입력 문자열에서 열린 괄호 ‘(’은 바로 놓인 그릇, 닫힌 괄호 ‘)’은 거꾸로 놓인 그릇을 나타난다. 문자열의 길이는 3이상 50 이하이다.

입력예시         출력예시
((((                25
()()()))(           80
)()((()             60
'''
plate = input("그릇이 놓인 형태 >>> ")
plate_list = list(plate)
length = 10

for i in range(1, len(plate_list)) :
    if plate_list[i-1] == plate_list[i] :
        length += 5
    else :
        length += 10
print(f"나열된 그릇의 총 길이 : {length}")