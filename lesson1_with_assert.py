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

        self.click_on_search(driver)
        self.put_apple_to_search(driver)
        self.click_on_categories(driver)
        self.click_on_button_search(driver)

    def click_on_button_search(self, driver):
        click_on_button_search = driver.find_element_by_css_selector(".col-sm-12 .btn.btn-primary").click()
        time.sleep(1)

    def click_on_categories(self, driver):
        click_on_categories = driver.find_element_by_css_selector('.col-sm-12 .row .col-sm-3').click()
        time.sleep(1)

    def put_apple_to_search(self, driver):
        put_apple_to_search = driver.find_element_by_css_selector("#search input").send_keys('apple')
        driver.find_element_by_css_selector("#search input").clear()
        driver.find_element_by_css_selector("#search input").send_keys('laptops')
        driver.find_element_by_css_selector(".btn.btn-default.btn-lg").click()
        time.sleep(1)

    def click_on_search(self, driver):
        click_on_search = driver.find_element_by_css_selector(".row ").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()

