# 성적처리 프로그램
'''
################################
#       성적처리프로그램       #
################################
1. 입력  |   2. 출력   | 3. 종료

'''
import os
file_path = "C:/Users/tpgns/Desktop/Coding_Practice/Python_Practice/score.txt"

print("################################")
print("#       성적처리프로그램       #")
print("################################")
print()
while True:
    print("1. 입력  |   2. 출력   | 3. 종료")
    select = int(input("실행할 항목을 선택하세요 >>> "))
    if select == 1:
        if os.path.isdir(file_path):            # \를 /로 변경
            f = open("C:/Users/tpgns/Desktop/Coding_Practice/Python_Practice/score.txt", 'w')
        else:
            f = open("C:/Users/tpgns/Desktop/Coding_Practice/Python_Practice/score.txt", 'a')
        info = []
        for i in range(4):
            if i == 0:
                info.append(str(input("이름 >>> ")))
                f.write(f"이름 : {info[i]}\n")
            else:
                info.append(int(input(f"점수{i} >>> ")))
                f.write(f"점수{i} : {info[i]}\n")
        f.write(f"총점 : {sum(info[1:])}\n")
        f.write(f"평균 : {sum(info[1:])/3}\n\n")
        f.close()
    elif select == 2:
        f = open(r'C:/Users/tpgns/Desktop/Coding_Practice/Python_Practice/score.txt', 'r')
        data = f.read()
        print(data)
        f.close
    elif select == 3:
        break
