# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from kontakt import kontakt
import unittest, time, re

class AddKontaktFirefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_kontakt_firefox(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, admin="admin", password="secret")
        self.add_new_record(driver, kontakt(username="First_name: Artur", middle_name="Middle_name: 123", last_name="Last_name: Piroshkov", nickname="Nickname: 123",
                            title="Title: addressbook", company="Company: OOO Privet", address="Address: Michurina 3", home="Home: 3",
                            mobile="Mobile: 9232847147", work="Work: None", fax="Fax: None", email="E-mail: 123@gmail.com",
                            email2="E-mail2: 234@gmail.com", email3="E-mail3: 345@gmail.com", homepage="Homepage: None", bday="28", bmonth="July", byear="1992",
                            aday="1", amonth="January", ayear="2000", secondary_address2="Secondary-address: Michurina 10", secondary_home2="Secondary-home: 10",
                            secondary_notes="Secondary-notes: None"))
        self.logout(driver)

    def test_add_kontakt_firefox2(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, admin="admin", password="secret")
        self.add_new_record(driver, kontakt(username="", middle_name="", last_name="", nickname="",
                            title="", company="", address="", home="",
                            mobile="", work="", fax="", email="",
                            email2="", email3="", homepage="", bday="28", bmonth="July", byear="1992",
                            aday="1", amonth="January", ayear="2000", secondary_address2="", secondary_home2="",
                            secondary_notes=""))
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def add_new_record(self, driver, kontakt):
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(kontakt.username)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(kontakt.middle_name)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(kontakt.last_name)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(kontakt.nickname)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(kontakt.title)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(kontakt.company)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(kontakt.address)
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(kontakt.home)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(kontakt.mobile)
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(kontakt.work)
        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(kontakt.fax)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(kontakt.email)
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(kontakt.email2)
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(kontakt.email3)
        driver.find_element_by_name("homepage").click()
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(kontakt.homepage)
        # choose bday
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(kontakt.bday)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[30]").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(kontakt.bmonth)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[41]").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(kontakt.byear)
        # anniversary (годовщина)
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text(kontakt.aday)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[3]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text(kontakt.amonth)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[35]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(kontakt.ayear)
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(kontakt.secondary_address2)
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(kontakt.secondary_home2)
        driver.find_element_by_name("notes").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(kontakt.secondary_notes)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def login(self, driver, admin, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(admin)
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_home_page(self, driver):
        driver.get("https://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
