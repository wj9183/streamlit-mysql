import mysql.connector
from mysql.connector import Error 

def main():
    try : 

        connection = mysql.connector.connect(
            host = 'database-1.czhazxqfdq7r.us-east-2.rds.amazonaws.com',
            database = 'yhdb',
            user = 'test_id',
            password = 'test1234'
        )

        if connection.is_connected() :
            cursor = connection.cursor(dictionary= True)
            query = """insert into cats (name, age) values (%s, %s);"""

            values = [("김선규", 5),
                      ("안토니오", 3),
                      ("말레피센트", 42)]
            cursor.executemany(query, values)
            
            connection.commit()




    except Error as e :
            print('디비 관련 에러 발생', e)
        
    finally :
        cursor.close()
        connection.close()
        print("MySQL 커넥션 종료")


if __name__ == '__main__':
    main()