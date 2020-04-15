import unittest, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from fixture.session import SessionHelper
# from fixture.group import GroupHelper




class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login_opencart(self):
        driver = self.driver
        driver.get("http://opencart.loc")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".collapse.navbar-collapse")))
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.session = SessionHelper(self)
    #     self.group = GroupHelper(self)

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
        click_on_register = driver.find_element_by_css_selector('.dropdown-menu.dropdown-menu-right li:nth-child(1)').click()
        time.sleep(1)

    def click_on_my_acc(self):
        driver = self.driver
        click_on_my_acc = driver.find_element_by_css_selector('.container #top-links .dropdown:nth-child(2)').click()
        time.sleep(1)

    def add_product_to_cart_in_case_of_empty_cart(self):
        driver = self.driver
        if driver.find_element_by_css_selector('#cart .dropdown-menu p').text == 'Your shopping cart is empty!':
            add_to_card_iphone = driver.find_element_by_css_selector(
                ' #common-home .row #content div:nth-child(2) .button-group button:nth-child(1)').click()
            time.sleep(1)
        else:
            pass

    def open_cart(self):
        driver = self.driver
        open_card = driver.find_element_by_css_selector('#cart-total').click()

    def destroy(self):
        self.driver.close()


