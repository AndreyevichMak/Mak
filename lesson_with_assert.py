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

        self.click_on_components(driver)
        assert "open" in driver.find_element_by_css_selector(".navbar-nav .dropdown:nth-child(3)").get_attribute("class")

        self.open_monitors(driver)
        assert "There are no products to list in this category." in driver.find_element_by_css_selector('#content p').text

    def open_monitors(self, driver):
        open_monitors = driver.find_element_by_css_selector(".navbar-nav .dropdown.open li:nth-child(3)").click()

    def click_on_components(self, driver):
        click_on_components = driver.find_element_by_xpath('*//nav//a[contains(text(), "Components")]').click()
        time.sleep(1)