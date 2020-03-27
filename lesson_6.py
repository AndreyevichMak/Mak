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

        self.click_on_desktops_all_desc(driver)

        assert 'Example of category description text' in driver.find_element_by_css_selector('#content .row .col-sm-10 ').text

    def click_on_desktops_all_desc(self, driver):
        click_on_desktops = driver.find_element_by_css_selector(
            '.container #menu div:nth-child(2) .nav li:nth-child(1) ').click()
        time.sleep(1)
        click_on_showalldesktops = driver.find_element_by_css_selector(
            '.dropdown.open .dropdown-menu .see-all ').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()