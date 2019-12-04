


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.chrome()
driver.get("http://testwisely.com/demo/helloworld")
try:
    driver.find_element_by_xpath ("/html/body/div[1]/section/section/div/p")
except NoSuchElementException:
    print ('no')
else:
    print ('yes')