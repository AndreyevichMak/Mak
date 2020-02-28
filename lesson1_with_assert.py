import unittest, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class admin_block_admin_access(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://opencart.loc")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".collapse.navbar-collapse")))
        try_to_click_on_search = driver.find_element_by_css_selector(".row ").click()
        time.sleep(1)
        put_apple_to_search = driver.find_element_by_css_selector("#search input").send_keys('apple')
        driver.find_element_by_css_selector("#search input").clear()
        driver.find_element_by_css_selector("#search input").send_keys('laptops')
        driver.find_element_by_css_selector(".btn.btn-default.btn-lg").click()
        time.sleep(1)
        #click_on_home = driver.find_element_by_css_selector('#product-search .breadcrumb li:nth-child(1)').click()
        click_on_categories = driver.find_element_by_css_selector('.col-sm-12 .row .col-sm-3').click()
        time.sleep(1)
        click_on_button_search = driver.find_element_by_css_selector(".col-sm-12 .btn.btn-primary").click()
        time.sleep(3)
        #assert "Your shopping cart is empty!" in driver.find_element_by_css_selector("p").text