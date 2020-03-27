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

        self.click_on_favorite(driver)
        self.click_on_camera(driver)
        self.add_to_card(driver)

    def add_to_card(self, driver):
        add_to_card = driver.find_element_by_css_selector(
            '#content .product-layout:nth-child(1) button:nth-child(1)').click()
        time.sleep(1)

    def click_on_camera(self, driver):
        click_on_camera = driver.find_element_by_css_selector('.nav.navbar-nav li:nth-child(7) ').click()
        time.sleep(1)

    def click_on_favorite(self, driver):
        click_on_favorite = driver.find_element_by_css_selector(
            '.row div:nth-child(3) .product-thumb .button-group').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()