'''
총 : 0개
--------------------------------------------------------------
번호    제목                    작성자      작성일      조회수
--------------------------------------------------------------
1       제목                    홍길동    2022-12-22     0
--------------------------------------------------------------
추가(A) 종료(X)

**************************************************************
제목 : 
내용 :
**************************************************************
제목 : 
내용 : 
--------------------------------------------------------------
수정(E) 삭제(D) 목록(L)

'''

import sqlite3
import datetime

#conn = sqlite3.connect('./Python_Practice/Py23.db')

class Post : 
    def user_check(id) :
        conn = sqlite3.connect('./Python_Practice/Py23.db')
        cursor = conn.cursor()
        sql = f"SELECT id FROM login_info WHERE login_id = ?"
        cursor.execute(sql, (id,))
        if cursor.fetchall() == [] :
            conn.close()
            return True
        else :
            conn.close()
            return False

    def user_join(id, pw) :
        conn = sqlite3.connect('./Python_Practice/Py23.db')
        cursor = conn.cursor()
        sql = f"INSERT INTO login_info(login_id, login_pw) VALUES(?,?)"
        cursor.execute(sql, (id,pw))
        conn.commit()
        conn.close()

    def login(login_id, login_pw) :
        conn = sqlite3.connect('./Python_Practice/Py23.db')
        cursor = conn.cursor()
        sql = "SELECT login_id, login_pw FROM login_info WHERE login_id = ? AND login_pw = ?"
        cursor.execute(sql, (login_id, login_pw))
        if cursor.fetchall() == [] :
            conn.close()
            return 0
        else :
            conn.close()
            print("로그인이 정상적으로 이루어졌습니다.\n")
            return 1

    def list() :
        conn = sqlite3.connect('./Python_Practice/Py23.db')
        cursor = conn.cursor()
        sql = "SELECT id, title, login_id, w_date, view_count FROM post_info"
        cursor.execute(sql)
        for row in cursor.fetchall() :
            print("%d       %-24s%s    %s     %d"%(row[0], row[1], row[2], row[3], row[4]))
        conn.close()

    def views(select_post) :
        conn = sqlite3.connect('./Python_Practice/Py23.db')
        cursor = conn.cursor()
        sql = "SELECT id, view_count FROM post_info WHERE id = ?"
        cursor.execute(sql, (select_post,))
        num = cursor.fetchone()[1]
        num += 1
        conn.close

        conn = sqlite3.connect('./Python_Practice/Py23.db')
        cursor = conn.cursor()
        sql = "UPDATE post_info SET view_count = ? WHERE id = ?"
        cursor.execute(sql, (num, select_post))
        conn.commit()
        conn.close()

    def detail(select_post) :
        conn = sqlite3.connect('./Python_Practice/Py23.db')
        cursor = conn.cursor()
        sql = "SELECT id, title, content, login_id FROM post_info WHERE id = ?"
        cursor.execute(sql, (select_post,))
        for row in cursor.fetchall() :
            print(f"제목   : {row[1]}")
            print(f"내용   : {row[2]}")
            print(f"작성자 : {row[3]}")
        conn.close()

    def insert(title, content, login_id, nowDate, view_count) :
        conn = sqlite3.connect('./Python_Practice/Py23.db')
        cursor = conn.cursor()
        sql = "INSERT INTO post_info(title, content, login_id, w_Date, view_count) VALUES(?, ?, ?, ?, ?)"
        cursor.execute(sql, (title, content, login_id, nowDate, view_count))
        conn.commit()
        conn.close()

    def update(select_post, title, content, login_id, nowDate) :
        conn = sqlite3.connect('./Python_Practice/Py23.db')
        cursor = conn.cursor()
        sql = "UPDATE post_info SET title = ?, content = ?, login_id = ?, w_Date = ? where id = ?"
        cursor.execute(sql, (title, content, login_id, nowDate, select_post))
        conn.commit()
        conn.close

#    def delete_all(self) :
#        pass

    def delete_part(select_post) :
        conn = sqlite3.connect('./Python_Practice/Py23.db')
        cursor = conn.cursor()
        sql = "DELETE FROM post_info WHERE id = ?"
        cursor.execute(sql, (select_post,))
        conn.commit()
        conn.close()

conn = sqlite3.connect('./Python_Practice/Py23.db')
cursor = conn.cursor()
sql = "SELECT id FROM post_info"
cursor.execute(sql)
Total_post = len(cursor.fetchall())
print(Total_post)
conn.close()

init_status = '등록된 게시글이 없습니다.'
page_num = 0
login_id = ''
login_pw = ''
select_post = 0
view_count = 0

# 메인 페이지
while True :
    print("\n-------------게시글 관리 프로그램-------------")
    user_status = input("로그인하기(L)  회원가입하기(J) 프로그램종료(X)\n\n>>> ")

    if user_status == 'L' or user_status == 'l' :
        print("------------로그인-------------")
        login_id = input("ID : ")
        login_pw = input("PW : ")
        login_status = Post.login(login_id, login_pw)

        if login_status == 1 :
            while page_num == 0 :
                print(f"총 : {Total_post}")
                print("--------------------------------------------------------------")
                print("번호    제목                    작성자      작성일      조회수")
                print("--------------------------------------------------------------")
                Post.list()
                print("--------------------------------------------------------------")
                fs = input("추가(A) 상세목록(L) 종료(X)\n\n>>> ")
                if fs == 'A' or fs == 'a' :
                    page_num = 1
                elif fs == 'L' or fs == 'l' :
                    select_post = int(input("상세 내용을 확인할 게시글 번호를 입력해주세요. >>> "))
                    Post.views(select_post)
                    page_num = 2
                elif fs == 'X' or fs == 'x' :
                    break
                else :
                    print("선택하신 항목이 존재하지 않습니다.\n")

                # DB 추가(insert)
                while page_num == 1 : 
                    title = input("제목 >>> ")
                    content = input("내용 >>> ")
                    now = datetime.datetime.now()
                    nowDate = now.strftime("%Y%m%d%H%M")
                    Post.insert(title, content, login_id, nowDate, view_count)
                    Total_post += 1
                    page_num = 0


                while page_num == 2 :
                    print("**************************************************************")
                    Post.detail(select_post)
                    print("**************************************************************")
                    fs = input("수정(E) 삭제(D) 목록으로 돌아가기(L)\n\n>>> ")
                    if fs == 'E' or fs == 'e' :
                        page_num = 3
                    elif fs == 'D' or fs == 'd' :
                        page_num = 4 # 해당 항목 삭제
                    elif fs == 'L' or fs == 'l' :
                        page_num = 0
                    else :
                        print("선택하신 항목이 존재하지 않습니다.\n")
                    
                    # DB 수정(update)
                    while page_num == 3 :
            #            update_post = int(input("수정할 게시글 번호를 입력해주세요. >>> "))
                        title = input("변경할 제목 (변경하지 않을 경우 x 입력) >>> ")
                        content = input("변경할 내용 (변경하지 않을 경우 x 입력) >>> ")
                        print("\n")
                        if title == 'X' or title == 'x' :
                            conn = sqlite3.connect('./Python_Practice/Py23.db')
                            cursor = conn.cursor()
                            sql = "SELECT title FROM post_info WHERE id = ?"
                            cursor.execute(sql, (select_post,))
                            title = cursor.fetchone()[0]
                        if content == 'X' or content == 'x' :
                            conn = sqlite3.connect('./Python_Practice/Py23.db')
                            cursor = conn.cursor()
                            sql = "SELECT content FROM post_info WHERE id = ?"
                            cursor.execute(sql, (select_post,))
                            content = cursor.fetchone()[0]
                        now = datetime.datetime.now()
                        nowDate = now.strftime("%Y%m%d%H%M")
            #            Post.update(update_post, title, content, login_id, nowDate)
                        Post.update(select_post, title, content, login_id, nowDate)
                        page_num = 2

                    # DB 삭제(delete)
                    while page_num == 4 :
            #            delete_type = input("전체삭제(A)  선택삭제(P)  상세목록으로 돌아가기(L)\n\n>>> ")
            #            if delete_type == 'A' or delete_type == 'a' :
            #                Post.delete_all(0)  #delete from DB
            #            elif delete_type == 'P' or delete_type == 'p' :
            #                delete_post = int(input("수정할 게시글 번호를 입력해주세요. >>> "))
            #                Post.delete_part(delete_post)
            #            elif delete_type == 'L' or delete_type == 'l' :
            #                page_num == 2
            #            else :
            #                print("선택하신 항목이 존재하지 않습니다.")

                        delete_type = input("정말 해당 게시글을 삭제하시겠습니까? (Y/N)\n\n>>> ")
                        if delete_type == 'Y' or delete_type == 'y' :
                            Post.delete_part(select_post)
                            print(f"{select_post}번 게시글이 정상적으로 삭제되었습니다.\n")
                            Total_post -= 1
                            page_num = 0
                        else :
                            page_num = 0

        else :
            print("로그인에 실패하셨습니다. 다시 시도해주세요.\n")
    
    elif user_status == "J" or user_status == "j" :
        while True :
            print("-------------회원가입--------------")
            id = input("사용할 ID : ")
            Post.user_check(id)
            if Post.user_check(id) == True :
                pw = input("사용할 PW : ")
                Post.user_join(id, pw)
                break
            else :
                print("중복된 계정이 존재합니다.\n")
                continue

    elif user_status == "X" or user_status == "x" :
        break