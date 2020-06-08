# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from lib.init import driver

class Module4LogoutByRecord(unittest.TestCase):
    
    def test_module4_logout_by_record(self):
        driver.get("https://dawnredwood-learninglog.herokuapp.com/")
        driver.find_element_by_link_text("log in").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("test")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("test123456")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("log out").click()


if __name__ == "__main__":
    unittest.main()
