#удаление группы.
from model.group import Group

def test_delete_first_group(app):
    #Если кол-во групп отсутствует - создаем группу, затем удаляем.
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="qweqwe"))
    app.group.delete_first_group()
