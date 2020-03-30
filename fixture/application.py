import unittest, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Application:
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://opencart.loc")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".collapse.navbar-collapse")))
    def __init__(self):
        self.driver = webdriver.Chrome()

    def click_on_login(self, mail, password):
        driver = self.driver
        click_on_login = driver.find_element_by_css_selector('.dropdown-menu.dropdown-menu-right li:nth-child(2)').click()
        time.sleep(1)
        driver.find_element_by_css_selector('.well .form-group input').send_keys('%s' % mail)
        time.sleep(1)
        driver.find_element_by_css_selector('[type="password"]').send_keys('%s.' % password)
        time.sleep(1)
        click_on_button_login = driver.find_element_by_css_selector('[type="submit"]').click()
        time.sleep(1)

    def click_on_continue(self):
        driver = self.driver
        click_on_continue = driver.find_element_by_css_selector('[type="submit"]').click()
        time.sleep(1)

    def click_on_button(self):
        driver = self.driver
        click_on_button = driver.find_element_by_css_selector('.buttons .pull-right input').click()
        time.sleep(1)

    def pesronal_details(self, name, password):
        driver = self.driver
        put_personal_details = driver.find_element_by_css_selector('#account div:nth-child(2) input').send_keys(
            '%s' % name)
        time.sleep(1)
        driver.find_element_by_css_selector('#account div:nth-child(4) input').send_keys('Andreyevich')
        time.sleep(1)
        driver.find_element_by_css_selector('#account div:nth-child(5) input').send_keys('makarenkoandrew@mail.ru')
        time.sleep(1)
        driver.find_element_by_css_selector('#account div:nth-child(6) input').send_keys('+97455468446')
        time.sleep(1)
        driver.find_element_by_css_selector('[type="password"]').send_keys('%s.' % password)
        time.sleep(1)
        driver.find_element_by_css_selector('fieldset:nth-child(2) div:nth-child(3) input').send_keys('Makpvl7.')
        time.sleep(1)

    def click_on_register(self):
        driver = self.driver
        click_on_register = driver.find_element_by_css_selector(
            '.dropdown-menu.dropdown-menu-right li:nth-child(1)').click()
        time.sleep(1)

    def click_on_my_acc(self):
        driver = self.driver
        click_on_my_acc = driver.find_element_by_css_selector('.container #top-links .dropdown:nth-child(2)').click()
        time.sleep(1)

    def destroy(self):
        self.driver.close()