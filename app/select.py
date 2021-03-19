import streamlit as st
import mysql.connector
from mysql.connector import Error

def select():

    column_list = ['title', 'author_fname', 'author_lname', 'released_year', 'stock_quantity', 'pages']

    selected_column_list = st.multiselect("컬럼을 선택하세요.", column_list)

    if len(selected_column_list) == 0:
        query = """select * from books; """
    else : 
        column_str = ', '.join(selected_column_list)
        query = "select book_id, " + column_str + ' from books;'


    try :
        connection = mysql.connector.connect(        # 이 함수를 가장 먼저 호출하고, 괄호 안에 정보를 넣어줘야한다 안그럼 개나소나 다 연결하니까.
            host = 'database-1.czhazxqfdq7r.us-east-2.rds.amazonaws.com',  
            database = 'yhdb',
            user = 'streamlit',
            password = 'yh1234' #원래 이런 정보들 여기에 안쓴다.
        )
        
        if connection.is_connected() :
            cursor = connection.cursor(dictionary = True)

            


           


    except Error as e :
        print('디비 관련 에러 발생', e)
    
    finally :
        # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
        #    커서와 커넥션을 모두 닫아준다.
        cursor.close()
        connection.close()
        print("MySQL 커넥션 종료")