import mysql.connector
from model.group import Group
from model.kontakt import Kontakt

class DbFixture:
    # autocommit=True кэш после каждого запроса сбрасывается.

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host,
                                                  database=name,
                                                  user=user,
                                                  password=password,
                                                  autocommit=True)

    # получение списка из БД.
    def get_group_list_db(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header from group_list")
            for row in cursor:
                # в каком порядке выстроить параметры.
                (id, name, header) = row
                list.append(Group(id=str(id), name=name, header=header))
        finally:
            cursor.close()
        return list

    # Выборка из БД id, firstname, lastname from addressbook где указаны текущие, а не все созданные.
    def get_kontakt_list_db(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                # в каком порядке выстроить параметры.
                (id, firstname, lastname) = row
                list.append(Kontakt(id=str(id), username=firstname, last_name=lastname))
        finally:
            cursor.close()
        return list

    def get_group_id_db(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                # в каком порядке выстроить параметры.
                (id) = row
                list.append(Kontakt(id=str(id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
