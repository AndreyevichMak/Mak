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
        click_on_mp3player= driver.find_element_by_css_selector('.container .collapse .nav li:nth-child(8) ').click()
        time.sleep(1)
        click_on_test= driver.find_element_by_css_selector('.dropdown.open .dropdown-menu  li:nth-child(1) ').click()
        time.sleep(1)
        assert 'There are no products to list in this category.' in driver.find_element_by_css_selector('#content ').text









    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()