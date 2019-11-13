from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

from fixture.group import KontaktHelper



class Application():
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        # open homepage
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

class Open_close_browser:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.kontakt = KontaktHelper(self)

    def open_start_page(self):
        wd = self.wd
        # open homepage
        wd.get("http://localhost/addressbook/")

    def exit_browser(self):
        self.wd.quit()
















