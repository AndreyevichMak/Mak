#import unittest, time
import pytest
from selenium import webdriver
from application import Application
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class admin_block_admin_access(unittest.TestCase):

    @pytest.fixture
    def app(request):
        fixture = Application()
        request.addfinalizer(fixture.destroy)
        return fixture

     def setUp(self):
         self.app = Application()
         self.driver = webdriver.Chrome()
    def test_search_in_python_org(app):
        driver = app.driver
        driver.get("http://opencart.loc")
        WebDriverWait(app.driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".collapse.navbar-collapse")))

        app.click_on_my_acc(app)
        app.click_on_register(app)
        app.pesronal_details( name='Mak', password='Makpvl7')
        app.click_on_button(app)
        app.click_on_continue(app)
        app.click_on_my_acc(app)
        app.click_on_login( mail='makarenkoandrew@mail.ru', password='Makpvl7')
        #assert "Warning: No match for E-Mail Address and/or Password." in driver.find_element_by_css_selector('.alert.alert-danger.alert-dismissible').text
    # def tearDown(self):
    #     self.app.destroy()
# if __name__ == "__main__":
#     unittest.main()