# Проверка подключения БД
# для коннектора 8.0.18
#import mysql.connector

# для pymysql лучше использовать этот отмечает Баранцев.
import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# с коннектором 8.0.18 mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    # необходим курсор для указания данных.
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()