'''
# Lora DB테이블에 장비 정보 입력, 수정, 삭제, 조회 프로그램 만들기
---------------------------------
1.입력 2.수정 3.삭제 4.조회 0.종료

'''

import sqlite3


def create() :
    conn = sqlite3.connect('DB.db')
    cursor = conn.cursor()
    dev_name = input("모뎀 이름 >>> ")
    dev_eui = input("DEV EUI >>> ")
    dev_app_key = input("DEV APP KEY >>> ")
    dev_app_eui = input("DEV_APP_EUI >>> ")
    sql = "INSERT INTO Lora_info(DEV_NAME, DEV_EUI, DEV_APP_KEY, DEV_APP_EUI) VALUES(?, ?, ?, ?)"
    cursor.excute(sql, (dev_name, dev_eui, dev_app_key, dev_app_eui))
    conn.commit()
    conn.exit()
    print("디바이스 등록이 완료되었습니다.")


def update() :
    while True :
        print("어떤 디바이스 내용을 수정하시겠습니까? (디바이스 넘버 입력, 0. 돌아가기)")
        dev_num = int(input(">>> "))
        if dev_num == 0 :
            break
        else :
            print("어떤 항목을 수정하시겠습니까?")
            print("1.전체 2.DEV_NAME 3.DEV_EUI 4.DEV_APP_KEY 5.DEV_APP_EUI 0.돌아가기")
            select = int(input(">>> "))
            try :
                if select == 0 :
                    break
                elif select == 1 :
                    conn = sqlite3.connect('DB.db')
                    cursor = conn.cursor()
                    dev_name = input("모뎀 이름 >>> ")
                    dev_eui = input("DEV EUI >>> ")
                    dev_app_key = input("DEV APP KEY >>> ")
                    dev_app_eui = input("DEV_APP_EUI >>> ")
                    sql = "UPDATE Lora_info SET DEV_NAME = ?, DEV_EUI = ?, DEV_APP_KEY = ?, DEV_APP_EUI = ? WHERE DEV_ID= ?"
                    cursor.execute(sql, (dev_name, dev_eui, dev_app_key, dev_app_eui, dev_num))
                    conn.commit()
                    conn.close()
                    break
                elif select == 2 :
                    conn = sqlite3.connect('DB.db')
                    cursor = conn.cursor()
                    dev_name = input("모뎀 이름 >>> ")
                    sql = "UPDATE Lora_info SET DEV_NAME = ? WHERE DEV_ID= ?"
                    cursor.execute(sql, (dev_name, dev_num))
                    conn.commit()
                    conn.close()
                    break
                elif select == 3 :
                    conn = sqlite3.connect('DB.db')
                    cursor = conn.cursor()
                    dev_eui = input("DEV EUI >>> ")
                    sql = "UPDATE Lora_info SET DEV_EUI = ? WHERE DEV_ID= ?"
                    cursor.execute(sql, (dev_name, dev_eui, dev_app_key, dev_app_eui, dev_num))
                    conn.commit()
                    conn.close()
                    break
                elif select == 4 :
                    conn = sqlite3.connect('DB.db')
                    cursor = conn.cursor()
                    dev_app_key = input("DEV APP KEY >>> ")
                    sql = "UPDATE Lora_info SET DEV_APP_KEY = ? WHERE DEV_ID= ?"
                    cursor.execute(sql, (dev_name, dev_eui, dev_app_key, dev_app_eui, dev_num))
                    conn.commit()
                    conn.close()
                    break
                elif select == 5 :
                    conn = sqlite3.connect('DB.db')
                    cursor = conn.cursor()
                    dev_app_eui = input("DEV_APP_EUI >>> ")
                    sql = "UPDATE Lora_info SET DEV_APP_EUI = ? WHERE DEV_ID= ?"
                    cursor.execute(sql, (dev_name, dev_eui, dev_app_key, dev_app_eui, dev_num))
                    conn.commit()
                    conn.close()
                    break         
            except :
                print("해당하는 항목이 없습니다.")

def delete() :
    while True :
        print("어떤 디바이스 내용을 삭제하시겠습니까? (디바이스 넘버 입력, 0. 돌아가기)")
        dev_num = int(input(">>> "))
        try :
            if dev_num == 0 :
                break
            conn = sqlite3.connect('DB.db')
            cursor = conn.cursor()
            sql = "DELETE FROM Lora_info WHERE DEV_NUM = ?"
            cursor.execute(sql, (dev_num, ))
            conn.commit()
            conn.close()
            break
        except :
            print("선택하신 디바이스 항목이 없습니다.")

def select() :
    while True :
        print("디바이스 정보 조회 방식을 선택하세요.")
        print("1.전체 2.선택 0.돌아가기")
        choice = int(input(">>> "))
        try :
            if choice == 0 :
                break
            elif choice == 1 :        
                conn = sqlite3.connect('DB.db')
                cursor = conn.cursor()
                sql = "SELECT * FROM Lora_info"
                cursor.execute(sql)
                for row in cursor.fetchall() :
                    print("%s %s %s %s %s"%(row[0], row[1], row[2], row[3], row[4]))
                cursor.close()
                break
            elif choice == 2 :
                print("디바이스 장비 번호를 입력하세요.")
                select = int(input(">>> "))
                conn = sqlite3.connect('DB.db')
                cursor = conn.cursor()
                sql = "SELECT * FROM Lora_info WHERE DEV_ID = ?"
                cursor.execute(sql, (select, ))
                cursor.close()
                break
        except :
            print("선택하신 항목이 존재하지 않습니다!")


while True :
    print("-----Lora 정보 관리 프로그램------")
    print("1.입력 2.수정 3.삭제 4.조회 0.종료")
    sel = int(input("항목을 선택하세요. >>> "))

    try :
        if sel == 1 : 
            create()
        elif sel == 2 :
            update()
        elif sel == 3 :
            delete()
        elif sel == 4 :
            select()
        elif sel == 0 :
            break
    except :
        print("선택하신 항목이 존재하지 않습니다!")