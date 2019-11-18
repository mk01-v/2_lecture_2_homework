from selenium.webdriver.support.ui import Select

class KontaktHelper:

    def __init__(self, app):
        self.app = app

    def open_kontakt_page(self):
        # open kontakt page
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_kontakt(self, kontakt):
        wd = self.app.wd
        self.open_kontakt_page()
        self.fill_kontakt_form(kontakt)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        self.return_to_main_home()

    def fill_kontakt_form(self, kontakt):
        wd = self.app.wd
        self.change_field_value_kontakt("firstname", kontakt.username)
        self.change_field_value_kontakt("middlename", kontakt.middle_name)
        self.change_field_value_kontakt("lastname", kontakt.last_name)
        self.change_field_value_kontakt("nickname", kontakt.nickname)
        self.change_field_value_kontakt("title", kontakt.title)
        self.change_field_value_kontakt("company", kontakt.company)
        self.change_field_value_kontakt("address", kontakt.address)
        self.change_field_value_kontakt("home", kontakt.home)
        self.change_field_value_kontakt("mobile", kontakt.mobile)
        self.change_field_value_kontakt("work", kontakt.work)
        self.change_field_value_kontakt("fax", kontakt.fax)
        self.change_field_value_kontakt("email", kontakt.email)
        self.change_field_value_kontakt("email2", kontakt.email2)
        self.change_field_value_kontakt("email3", kontakt.email3)
        self.change_field_value_kontakt("homepage", kontakt.homepage)

        self.change_field_value_kontakt_selector("bday", kontakt.bday)
        self.change_field_value_kontakt_selector("bmonth", kontakt.bmonth)
        self.change_field_value_kontakt("byear", kontakt.byear)

        # anniversary (годовщина)
        self.change_field_value_kontakt_selector("aday", kontakt.aday)
        self.change_field_value_kontakt_selector("amonth", kontakt.amonth)
        self.change_field_value_kontakt("ayear", kontakt.ayear)

        self.change_field_value_kontakt("address2", kontakt.secondary_address2)
        self.change_field_value_kontakt("phone2", kontakt.secondary_home2)
        self.change_field_value_kontakt("notes", kontakt.secondary_notes)

    def change_field_value_kontakt_selector(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value_kontakt(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modif_kontakt(self, kontakt):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_kontakt_form(kontakt)
        wd.find_element_by_name("update").click()

    def delete_kontakt(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # закрытие диалогового окна подтверждением.
        wd.switch_to_alert().accept()
        self.return_to_main_home()

    def return_to_main_home(self):
        wd = self.app.wd
        # return groups page
        wd.find_element_by_link_text("home").click()

    # подсчет количества контактов. Необходимость: проверка перед выполнением теста - создавать или нет предварительно контакт.
    def count_kontakt(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))