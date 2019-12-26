from model.group import Group
from selenium.webdriver.support.ui import Select


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        # open groups page
        #wd.find_element_by_link_text("groups").click()
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        # сбрасываем кэш, т.к. после операции является не валидным.
        self.group_cache = None

    #def modify_first_group(self, new_group_data):
    #    wd = self.app.wd
    #    self.open_group_page()
    #    self.select_first_group()
    #    # open modification page
    #    wd.find_element_by_name("edit").click()
    #    self.fill_group_form(new_group_data)
    #    # submit modification
    #    wd.find_element_by_name("update").click()
    #    self.return_to_group_page()
    #    # сбрасываем кэш, т.к. после операции является не валидным.
    #    self.group_cache = None

    #удаление будет выполняться также как и раньше.
    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # open modification page
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        # сбрасываем кэш, т.к. после операции является не валидным.
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    #def delete_first_group(self):
    #    wd = self.app.wd
    #    self.open_group_page()
    #    self.select_first_group()
    #    wd.find_element_by_name("delete").click()
    #    self.return_to_group_page()
    #    # сбрасываем кэш, т.к. после операции является не валидным.
    #    self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    #удаление будет выполняться также как и раньше.
    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        # сбрасываем кэш, т.к. после операции является не валидным.
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        # сбрасываем кэш, т.к. после операции является не валидным.
        self.group_cache = None

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    # заводим переменную для кэша.
    group_cache = None

    def get_group_list(self):
        # делаем проверку.
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            # Проверка по наименованию групп.
            # Проверить можно в браузере что выберется. Ввести в консоли f12 $$('span.group').
            for element in wd.find_elements_by_css_selector("span.group"):
                # get_text() - вызывает метод, а нужно обращаться к свойству текст: text.
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
            # возращаем копию кэша.
        return list(self.group_cache)



