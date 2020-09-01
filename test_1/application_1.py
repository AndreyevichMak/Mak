import unittest, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def login_opencart(self):
        driver = self.driver
        driver.get("http://opencart.loc/")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#top')))


    def check_if_else_item(self):
        driver = self.driver
        if driver.find_element_by_css_selector('#cart .table'):
            print('item is here')
        else:
            print('item is not here')

    def click_on_addtocart_nikonD300(self):
        driver = self.driver
        click_on_addtocart_nikonD300 = driver.find_element_by_css_selector(
            '#content .row div:nth-child(2) .product-thumb .button-group button').click()
        time.sleep(2)


    def click_on_list(self):
        driver = self.driver
        click_on_list = driver.find_element_by_css_selector('.row .btn-group #list-view').click()
        time.sleep(1)


    def click_on_sort_by(self):
        driver = self.driver
        click_on_sort_by = driver.find_element_by_css_selector(
            '#product-category .row #content .row div:nth-child(3) .form-group #input-sort ').click()
        time.sleep(1)

    def click_on_cameras(self):
        driver = self.driver
        click_on_cameras = driver.find_element_by_css_selector(
            '.container #menu .collapse .nav li:nth-child(7)').click()
        time.sleep(1)

    def check_shopping_cart(self):
        driver = self.driver
        check_shopping_cart = driver.find_element_by_css_selector('#cart-total').click()
        time.sleep(1)

    def destroy(self):
        self.driver.close()