from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.kontakt import KontaktHelper


class Application:
    def __init__(self, browser="Firefox"):
        if browser == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser == "Chrome":
            self.wd = webdriver.Chrome('C:\Python\Projects\2_lecture_2_homework\env\Lib\site-packages\selenium\webdriver\chrome\webdriver.exe')
        elif browser == "Opera":
            self.wd = webdriver.Opera()
        elif browser == "Ie":
            self.wd = webdriver.Ie()
        else:
            # если ничего не нашли. Raise - аварийное прерывание конструкции.
            raise ValueError("Unrecognized browser %s" % browser)
        #период ожидания драйвером дождаться элементов
        #для динамических элменетов, если данные присутствуют на странице сразу - можно убрать.
        self.wd.implicitly_wait(7)
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
















