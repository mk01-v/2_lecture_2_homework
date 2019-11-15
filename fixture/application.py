from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.kontakt import KontaktHelper


class Application():
    def __init__(self):
        self.wd = webdriver.Firefox()
        #период ожидания драйвером дождаться элементов
        #для динамических элменетов, если данные присутствуют на странице сразу - можно убрать.
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.kontakt = KontaktHelper(self)

    #Проверка текущей страницы.
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        # open homepage
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
















