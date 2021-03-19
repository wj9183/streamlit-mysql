import streamlit as st
import mysql.connector
from mysql.connector import Error


def main():

    book_id_list = []

    try : 
        # 1. 커넉터로부터 커넥션을 받는다.
        connection = mysql.connector.connect(
            host = '',
            database = '',
            user = '',
            password = ''
        )

        if connection.is_connected() :
            cursor = connection.cursor(dictionary= True)
            query = """ select *
                        from books limit 5; """
            cursor.execute(query)
            results = cursor.fetchall()

            for row in results :
                st.write(row)
                book_id_list.append( row['book_id'] )


    except Error as e :
            print('디비 관련 에러 발생', e)
        
    finally :
        # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
        #    커서와 커넥션을 모두 닫아준다.
        cursor.close()
        connection.close()
        print("MySQL 커넥션 종료")


    book_id = st.number_input('책 아이디 입력', 
                                min_value= book_id_list[0],
                                max_value= book_id_list[-1])
    stock_quantity = st.number_input('수량 입력', min_value=0)
    pages = st.number_input('페이지 입력', min_value=1)


    if st.button('실행') :
    
        try :
            # 1. 커넉터로부터 커넥션을 받는다.
            connection = mysql.connector.connect(
                host = 'database-1.c51w3te8io5h.ap-northeast-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = 'yh1234'
            )
            
            if connection.is_connected() :
                # 2. 커서를 가져온다.
                cursor = connection.cursor()

                # 3. 우리가 원하는거 실행 가능.      
                query = """ update books
                            set pages = %s, stock_quantity = %s 
                            where book_id = %s; """
                
                data = (pages, stock_quantity, book_id)

                cursor.execute(query, data)

                connection.commit()
                        
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
