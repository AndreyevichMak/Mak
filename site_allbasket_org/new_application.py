import unittest, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class New_Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login_to_allbasketorg(self):
        driver = self.driver
        driver.get("https://allbasketball.org/")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#login-modal')))




    def click_on_players(self):
        driver = self.driver
        click_on_players = driver.find_element_by_css_selector(
        '.header-menu .navbar .container .collapse .nav.navbar-nav .dropdown:nth-child(8)').click()
        time.sleep(1)


    def destroy(self):
        self.driver.close()
