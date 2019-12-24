from pony.orm import *
from datetime import datetime
from model.group import Group
from model.kontakt import Kontakt
# в новой версии pony имеется нормальное преобразование данных, написано без дополнений. "#, conv=decoders)"
#from pymysql.converters import decoders

# другая техника взаимодействия с БД "ORM", чтобы не учить язык sql.
# позволяет установить соответствия с классами и таблицами в БД.
# автоматически генерируют запросы sql.
class ORMFixture:
    # объект на основании которого будем строить привязки.
    db = Database()
    # набор свойств и привязать их к полям таблицы.
    # db.Entity класс описывает какие-то объекты, которые будут сохраняться в эту базу данных.
    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')

    class ORMKontakt(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    # привязка к БД.
    def __init__(self, host, name, user, password):
        # 1 - параметр тип базы данных.
        self.db.bind('mysql', host=host, database=name, user=user, password=password) #, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    # нечитаемый вывод групп - обозначено как ORMGroup[123]. Данная функция исправляет.
    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header)
        return list(map(convert, groups))


    # получение списков объектов.
    # блок кода должен выполняться в рамках сессии - db_session.
    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_kontakts_to_model(self, kontakts):
        def convert(kontakt):
            return Kontakt(id=str(kontakt.id), username=kontakt.firstname, last_name=kontakt.lastname)
        return list(map(convert, kontakts))

    @db_session
    def get_kontact_list(self):
        return self.convert_kontakts_to_model(select(c for c in ORMFixture.ORMKontakt if c.deprecated is None))
