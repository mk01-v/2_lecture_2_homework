from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
# проверка загрузки данных контактов.
try:
    kontakts = db.get_kontakt_list_db()
    for kontakt in kontakts:
        print(kontakt)
    print(len(kontakts))
finally:
    db.destroy()


#--------------------------------------
# Проверка подключения БД
# для коннектора 8.0.18
#import mysql.connector

# для sql лучше использовать этот драйвер отмечает Баранцев.
#import pymysql.cursors

#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# с коннектором 8.0.18 mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#try:
#    # необходим курсор для указания данных.
#    cursor = connection.cursor()
#    cursor.execute("select * from group_list")
#    for row in cursor.fetchall():
#        print(row)
#finally:
#    connection.close()