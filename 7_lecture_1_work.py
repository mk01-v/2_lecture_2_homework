# Проверка подключения БД
import mysql.connector

connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    pass
finally:
    connection.close()