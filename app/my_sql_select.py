import streamlit as st
import mysql.connector
from mysql.connector import Error

import numpy as np
import pandas as pd
import json

def my_sql_select():

    column_list = ['title', 'author_fname', 'author_lname', 'released_year', 'stock_quantity', 'pages']

    selected_column_list = st.multiselect("컬럼을 선택하세요.", column_list)

    if len(selected_column_list) == 0:
        query = """select * from books; """
    else : 
        column_str = ', '.join(selected_column_list)
        # st.write(column_str)      #쿼리문에 넣기 전에 문자열이 잘 이어져서 나오는지 테스트해보자.
        query = "select book_id, " + column_str + ' from books;'
        #st.write(query)  #쿼리도 화면에 표시해서 제대로 나오나 보자
    #st.write(query)       #선택을 아무것도 안하면 뭐가 나오는지도 확인해보자




    try :
        connection = mysql.connector.connect(        # 이 함수를 가장 먼저 호출하고, 괄호 안에 정보를 넣어줘야한다 안그럼 개나소나 다 연결하니까.
            host = 'database-1.czhazxqfdq7r.us-east-2.rds.amazonaws.com',  
            database = 'yhdb',
            user = 'streamlit',
            password = 'yh1234' #원래 이런 정보들 여기에 안쓴다.
        )
        
        if connection.is_connected() :
            cursor = connection.cursor(dictionary = True)
            #2. 쿼리 만들어서 실행
            cursor.execute(query)        #쿼리랑 파라미터를 넣는다.
            #3. select 이므로, fetchall 한다.
            results = cursor.fetchall()      #페치하면 항상 반복해야한다. 아예 없거나 여러개라.

            st.write(results)

            json_results = json.dumps(results)          #파이썬의 리스트 + 딕셔너리 조합을 => JSON 형식으로 바꾸는 것. 키값이 따옴표가 아닌 쌍따옴표로 처리된다.

            #판다스의 데이터프레임으로 읽을 것이다.
            df = pd.read_json(json_results)     #제이슨을 읽어오는 함수가 있네

            st.dataframe(df)


            st.dataframe(results)              #이렇게 해도 되긴 되는데 하지 마라. 나중에 언젠가는 버그가 날 가능성이 높다. 제이슨은 따옴표는 늘 쌍따옴표고, 리스트는 그냥 따옴표일 확률이 높아서.





            


           


    except Error as e :
        print('디비 관련 에러 발생', e)
    
    finally :
        # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
        #    커서와 커넥션을 모두 닫아준다.
        cursor.close()
        connection.close()
        print("MySQL 커넥션 종료")