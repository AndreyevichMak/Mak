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

        self.click_on_shoppingcart(driver)

        assert 'Your shopping cart is empty!' in driver.find_element_by_css_selector('#error-not-found .row #content').text

    def click_on_shoppingcart(self, driver):
        click_on_shoppingcart = driver.find_element_by_css_selector(
            '#top .container #top-links .list-inline li:nth-child(4)').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()