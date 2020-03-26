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
        driver.get("https://allbasketball.org/")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#login-modal')))
        click_on_players = driver.find_element_by_css_selector('.header-menu .navbar .container .collapse .nav.navbar-nav .dropdown:nth-child(8)').click()
        time.sleep(5)




    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()