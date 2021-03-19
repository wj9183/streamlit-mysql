import streamlit as st
import mysql.connector
from mysql.connector import Error
from select import select



def main():


    menu = ['Select', 'Insert', 'Update', 'Delete']  #사이드바 메뉴할 거 4개.
    choice = st.sidebar.selectbox("메뉴", menu)  


    if choice == 'Select':
        select()
       