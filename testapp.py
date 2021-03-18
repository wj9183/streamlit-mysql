import streamlit as st
import mysql.connector #조금 전에 다운로드 받은 라이브러리.
from mysql.connector import Error #데이터베이스 관련한 에러는 얘가 잡아줄 것임. 데이터베이스 연결이 안되거나 쿼리를 이상하게 쓰거나 했을 때 등의 여러가지 에러
from datetime import datetime, date, time


def main():
    # name = st.text_input("이름을 입력하세요.")
    # birth_date = st.date_input("생년월일 입력하세요.")
    # birth_time = st.time_input("태어난 시간 입력하세요.")
    # birth_dt = datetime.combine(birth_date, birth_time)

    # print(type(birth_date))
    # print(type(birth_time))
    # print(type(birth_dt))

    if st.button('저장'):


        try :      #트라이문 안에서 에러가 생기면 에러 생겼을 때 어떻게 하겠다고 처리해줄 수가 있다. 예를 들어 쿼리문을 잘못써서 에러가 나면. 한참 밑에 try랑 동등한 레벨의 except
            #1. 커넥터로부터 커넥션을 받는다.
            connection = mysql.connector.connect(        # 이 함수를 가장 먼저 호출하고, 괄호 안에 정보를 넣어줘야한다 안그럼 개나소나 다 연결하니까.
                host = 'database-1.czhazxqfdq7r.us-east-2.rds.amazonaws.com',       #이 주소?를 엔드포인트라고한다. database-1.czhazxqfdq7r.us-east-2.rds.amazonaws.com
                database = 'yhdb',
                user = 'streamlit',
                password = 'yh1234' #원래 이런 정보들 여기에 안쓴다.
            )
            print(connection)

            if connection.is_connected():               #연결되어있니?      #이거 다 마이에스큐엘 커넥터 라이브러리에서 주는 거임.
                print('연결 됐을 때 디버깅')                #연결 됐는지 확인하고 싶으면 절차마다 찍어봐라. 이런게 디버깅이다.
                db_info = connection.get_server_info()   #커넥션 맺은 서버의 정보를 가져와라ㅏ. 서버 버전이 들어있다.
                print("MySQL server version : ", db_info)

                # 2. 커서를 가져온다.
                cursor = connection.cursor()

                print('커서 가져오고 나서 디버깅')

                # 3. 이제 우리가 원하는 거 실행 가능하다.
                # cursor.execute('select database();')    # 괄호 안에 쿼리문을 써준다. 쿼리를 실행하라는 뜻.

                #이제 데이터 인서트를 해본다.
                # query = """ insert into books (title, author_fname,
                #         author_lname, released_year, stock_quantity, pages)
                #         values (%s, %s, %s, %s, %s, %s);""" 
                #                                                                                     # %s는 숫자인지 소문자인지 상관없이 알아서 넣어준다.
                # record = (title, author_fname, author_lname, released_year, stock_quantity, pages)      #리스트 말고 튜플이여야 한다.
                

                query = """ insert into cats4(name, age)
                        values (%s, %s);""" 
                                                                                                    # %s는 숫자인지 소문자인지 상관없이 알아서 넣어준다.
                record = [('냐웅이', 1 ), ('나비', 3), ('단비', 5), ]      #하나의 데이터는 꼭 튜플로 넣어야한다 하지만 넣어야할 데이터가 여러개면 당연히 그걸 리스트로 묶는다. 일관성이 있다.

                print()

                cursor.executemany(query, record)          #여러개 저장할 땐 executemany
                connection.commit()    #커밋해라 데이터베이스에 영구 저장해라
                print("{}개 적용됨".format(cursor.rowcount))
                st.success('저장되었습니다.')
                # 4. 위의 실행한 결과는 커서에 들어있다. 실행후 커서에서 결과를 빼낸다.
                # record = cursor.fetchone() 커밋하는 건 결과를 셀렉트해오는 게 아니기 때문에 이 줄이 필요 없다.
                # print('Connected to db : ', record) # db이름 찍어보기

                ####순서####    연결하고 커서 가져오고 원하는 sql문 실행시키고 실행한 결과를 화면에 보여주면 된다.
        except Error as e :
            print('DB 관련 에러 발생', e)
        finally :    #트라이에 걸리든 익셉트에 걸리든 마지막엔...
            #5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
            #   커서와 커넥션을 모두 닫아준다.
            cursor.close()      #커서부터 연결을 끊어줘야함. 커넥션부터 끊으면 다른 거 못한다.
            connection.close()
            print("MySQL 커넥션 종료")   #커넥션을 다시 얻어오기 전까지 이제 실행 못하게 된다.



if __name__ == '__main__':
    main()



#파이썬에서 마이에스큐엘 접속할 수 있는 라이브러리들이 몇가지 있다. 그것 중 하나를 깔아야한다.

#디버깅은 프린트문으로 한다.