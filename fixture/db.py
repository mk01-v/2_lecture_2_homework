import mysql.connector
from model.group import Group

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host,
                                                  database=name,
                                                  user=user,
                                                  password=password)

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

    def destroy(self):
        self.connection.close()
