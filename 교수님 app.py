import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time


def main():
    # title = st.text_input('책 제목 입력')
    # author_fname = st.text_input('이름 입력')
    # author_lname = st.text_input('성 입력')
    # released_year = st.number_input('년도 입력')
    # stock_quantity = st.number_input('수량 입력')
    # pages = st.number_input('페이지입력')

    # name = st.text_input('이름 입력')
    # birth_date = st.date_input('생년월일')
    # birth_time = st.time_input('시간입력')
    
    # birth_dt = datetime.combine(birth_date, birth_time)
    
    # print(birth_date)
    # print(birth_time)
    # print(birth_dt)

    st.subheader('몇년도 이후, 몇페이지 이상되는 책을 검색하고 싶으십니까?')
    released_year = st.number_input('년도 입력', min_value=1800, max_value=2050)
    pages = st.number_input('페이지수 입력', min_value=10)

    order = 'asc'
    if st.checkbox("오름차순 / 내림차순") :
        order = 'desc'
    
    if st.button('조회') :

        try :
            # 1. 커넉터로부터 커넥션을 받는다.
            connection = mysql.connector.connect(
                host = ' ',
                database = ' ',
                user = ' ',
                password = ' '
            )
            
            if connection.is_connected() :
                db_info = connection.get_server_info()
                print("MySQL server version : ", db_info)

                # 2. 커서를 가져온다.
                cursor = connection.cursor()

                # 3. 우리가 원하는거 실행 가능.            
                query = """select * from books;"""
                
                cursor.execute(query)

                
                # 4. 실행 후 커서에서 결과를 빼낸다. 
                
                results = cursor.fetchall()

                
                print(results)

                # for data in results :
                #     print(data[1] , data[4])

                
                cursor = connection.cursor(dictionary= True)

                if order == 'asc' :
                    query = """ select title, released_year, pages
                            from books
                            where released_year > %s and pages > %s
                            order by released_year asc ; """
                else :
                    query = """ select title, released_year, pages
                            from books
                            where released_year > %s and pages > %s
                            order by released_year desc ; """
                         
                param = (released_year, pages)

                cursor.execute(query, param)
                results = cursor.fetchall()
                
                for data in results :
                    print(data['title'], data['released_year'])
                    st.write(data)

        
        except Error as e :
            print('디비 관련 에러 발생', e)
        
        finally :
            # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
            #    커서와 커넥션을 모두 닫아준다.
            cursor.close()
            connection.close()
            print("MySQL 커넥션 종료")

if __name__ == '__main__' :    
    main()