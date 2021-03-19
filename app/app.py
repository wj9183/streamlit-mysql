import streamlit as st
import mysql.connector
from mysql.connector import Error
from my_sql_select import my_sql_select



def main():


    menu = ['Select', 'Insert', 'Update', 'Delete']  #사이드바 메뉴할 거 4개.
    choice = st.sidebar.selectbox("메뉴", menu)  


    if choice == 'Select':
        my_sql_select()



if __name__ == '__main__':
    main()
       