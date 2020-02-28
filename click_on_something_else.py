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
        click_on_featured_mac_ = driver.find_element_by_css_selector(".row .image").click()
        time.sleep(1)
        click_on_img_macbook = driver.find_element_by_id('content').click()
        time.sleep(1)
        click_on_next_button = driver.find_element_by_css_selector("button.mfp-arrow-right").click()
        time.sleep(1)
        click_on_next_button = driver.find_element_by_css_selector("button.mfp-arrow-right").click()
        time.sleep(1)
        click_on_next_button = driver.find_element_by_css_selector("button.mfp-arrow-right").click()
        time.sleep(1)
        click_on_next_button = driver.find_element_by_css_selector("button.mfp-arrow-right").click()
        time.sleep(1)
        click_on_next_button = driver.find_element_by_css_selector("button.mfp-arrow-right").click()
        time.sleep(1)
