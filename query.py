import mysql.connector
import streamlit as st

#connection

conn=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="",
    db="mydb"
)
c=conn.cursor()

#fetch

def view_all_data():
    c.execute('select * from Book2')
    data=c.fetchall()
    return data