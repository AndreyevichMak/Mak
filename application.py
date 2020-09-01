import unittest, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login_opencart(self):
        driver = self.driver
        driver.get("http://opencart.loc")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".collapse.navbar-collapse")))


    def click_on_login(self, mail, password):
        driver = self.driver
        click_on_login = driver.find_element_by_css_selector('.dropdown-menu.dropdown-menu-right li:nth-child(2)').click()
        time.sleep(1)
        driver.find_element_by_css_selector('.well .form-group input').send_keys('%s' % mail)
        time.sleep(1)
        driver.find_element_by_css_selector('[type="password"]').send_keys('%s.' % password)
        time.sleep(1)
        click_on_button_login = driver.find_element_by_css_selector('[type="submit"]').click()
        time.sleep(1)

    def click_on_continue(self):
        driver = self.driver
        click_on_continue = driver.find_element_by_css_selector('[type="submit"]').click()
        time.sleep(1)

    def click_on_button(self):
        driver = self.driver
        click_on_button = driver.find_element_by_css_selector('.buttons .pull-right input').click()
        time.sleep(1)

    def pesronal_details(self, name, password):
        driver = self.driver
        put_personal_details = driver.find_element_by_css_selector('#account div:nth-child(2) input').send_keys(
            '%s' % name)
        time.sleep(1)
        driver.find_element_by_css_selector('#account div:nth-child(4) input').send_keys('Andreyevich')
        time.sleep(1)
        driver.find_element_by_css_selector('#account div:nth-child(5) input').send_keys('makarenkoandrew@mail.ru')
        time.sleep(1)
        driver.find_element_by_css_selector('#account div:nth-child(6) input').send_keys('+97455468446')
        time.sleep(1)
        driver.find_element_by_css_selector('[type="password"]').send_keys('%s.' % password)
        time.sleep(1)
        driver.find_element_by_css_selector('fieldset:nth-child(2) div:nth-child(3) input').send_keys('Makpvl7.')
        time.sleep(1)

    def click_on_register(self):
        driver = self.driver
        click_on_register = driver.find_element_by_css_selector('.dropdown-menu.dropdown-menu-right li:nth-child(1)').click()
        time.sleep(1)

    def click_on_my_acc(self):
        driver = self.driver
        click_on_my_acc = driver.find_element_by_css_selector('.container #top-links .dropdown:nth-child(2)').click()
        time.sleep(1)

    def add_product_to_cart_in_case_of_empty_cart(self):
        driver = self.driver
        if driver.find_element_by_css_selector('#cart .dropdown-menu p').text == 'Your shopping cart is empty!':
            add_to_card_iphone = driver.find_element_by_css_selector('#common-home .row #content div:nth-child(2) .button-group button:nth-child(1)').click()
            time.sleep(1)
        else:
            pass

    def open_cart(self):
        driver = self.driver
        open_cart = driver.find_element_by_css_selector('#cart-total').click()

    def click_on_button_search(self):
        driver = self.driver
        click_on_button_search = driver.find_element_by_css_selector(".col-sm-12 .btn.btn-primary").click()
        time.sleep(1)

    def click_on_categories(self):
        driver = self.driver
        click_on_categories = driver.find_element_by_css_selector('.col-sm-12 .row .col-sm-3').click()
        time.sleep(1)

    def put_apple_to_search(self):
        driver = self.driver
        put_apple_to_search = driver.find_element_by_css_selector("#search input").send_keys('apple')
        driver.find_element_by_css_selector("#search input").clear()
        driver.find_element_by_css_selector("#search input").send_keys('laptops')
        driver.find_element_by_css_selector(".btn.btn-default.btn-lg").click()
        time.sleep(1)

    def click_on_search(self):
        driver = self.driver
        click_on_search = driver.find_element_by_css_selector(".row ").click()
        time.sleep(1)

    def add_to_card(self):
        driver = self.driver
        add_to_card = driver.find_element_by_css_selector('#content .product-layout:nth-child(1) button:nth-child(1)').click()
        time.sleep(5)

    def click_on_camera(self):
        driver = self.driver
        click_on_camera = driver.find_element_by_css_selector('.nav.navbar-nav li:nth-child(7) ').click()
        time.sleep(1)

    def click_on_favorite(self):
        driver = self.driver
        click_on_favorite = driver.find_element_by_css_selector('.row div:nth-child(3) .product-thumb .button-group').click()
        time.sleep(1)


    def click_on_shoppingcart(self):
        driver = self.driver
        click_on_shoppingcart = driver.find_element_by_css_selector('#top .container #top-links .list-inline li:nth-child(4)').click()
        time.sleep(1)

    def click_on_burger_menu(self):
        driver = self.driver
        click_on_burger_menu = driver.find_element_by_css_selector('.header .header__content .wrapper.nav-wrapper .nav-ul li:nth-child(3)').click()
        time.sleep(1)

    def click_on_desktops_all_desc(self):
        driver = self.driver
        click_on_desktops = driver.find_element_by_css_selector('.container #menu div:nth-child(2) .nav li:nth-child(1) ').click()
        time.sleep(1)
        click_on_showalldesktops = driver.find_element_by_css_selector('.dropdown.open .dropdown-menu .see-all ').click()
        time.sleep(1)

    def click_on_test(self):
        driver = self.driver
        click_on_test = driver.find_element_by_css_selector('.dropdown.open .dropdown-menu  li:nth-child(1) ').click()
        time.sleep(1)

    def click_on_mp3player(self):
        driver = self.driver
        click_on_mp3player = driver.find_element_by_css_selector('.container .collapse .nav li:nth-child(8) ').click()
        time.sleep(1)


    def click_on_navbar_dropdown_menu_PC0(self):
        driver = self.driver
        click_on_navbar_dropdown_menu_PC0 = driver.find_element_by_css_selector(".navbar .dropdown li:nth-child(1)").click()
        time.sleep(1)

    def click_on_navbar_desctop(self):
        driver = self.driver
        click_on_navbar_desctop = driver.find_element_by_css_selector(".navbar .collapse.navbar-collapse li:nth-child(1)").click()
        time.sleep(1)

    def click_on_add(self):
        driver = self.driver
        click_on_add = driver.find_element_by_id('button-cart').click()
        time.sleep(1)

    def click_on_products(self):
        driver = self.driver
        click_on_products = driver.find_element_by_css_selector(".product-thumb").click()
        time.sleep(1)

    def click_on_mp3_players_in_navbar(self):
        driver = self.driver
        click_on_mp3_players_in_navbar = driver.find_element_by_css_selector(".navbar :nth-child(8)").click()
        time.sleep(1)

    def click_on_cameras_in_navbar(self):
        driver = self.driver
        click_on_cameras_in_navbar = driver.find_element_by_css_selector(".navbar :nth-child(7)").click()
        time.sleep(1)

    def click_on_phones_pdas_in_navbar(self):
        driver = self.driver
        click_on_phones_pdas_in_navbar = driver.find_element_by_xpath('*//nav//a[contains(text(), "Phones & PDAs")]').click()
        time.sleep(1)

    def click_on_software_in_navbar(self):
        driver = self.driver
        click_on_software_in_navbar = driver.find_element_by_xpath('*//nav//a[contains(text(), "Software")]').click()
        time.sleep(1)

    def click_on_tablets_in_navbar(self):
        driver = self.driver
        click_on_tablets_in_navbar = driver.find_element_by_xpath('*//nav//a[contains(text(), "Tablets")]').click()
        time.sleep(1)

    def click_on_components_in_navbar(self):
        driver = self.driver
        click_on_components_in_navbar = driver.find_element_by_xpath('*//nav//a[contains(text(), "Components")]').click()
        time.sleep(1)

    def click_on_laptops_in_navbar(self):
        driver = self.driver
        click_on_laptops_in_navbar = driver.find_element_by_xpath('*//nav//a[contains(text(), "Laptops & Notebooks")]').click()
        time.sleep(1)

    def click_on_desktops_in_navbar(self):
        driver = self.driver
        click_on_desktops_in_navbar = driver.find_element_by_xpath('*//nav//a[contains(text(), "Desktops")]').click()
        time.sleep(1)

    def click_on_next_button(self):
        driver = self.driver
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

    def click_on_img_macbook(self):
        driver = self.driver
        click_on_img_macbook = driver.find_element_by_id('content').click()
        time.sleep(1)

    def click_on_featured_mac_(self):
        driver = self.driver
        click_on_featured_mac_ = driver.find_element_by_css_selector(".row .image").click()
        time.sleep(1)

    def click_on_navbar_dropdown_menu_PC0(self):
        driver = self.driver
        click_on_navbar_dropdown_menu_PC0 = driver.find_element_by_css_selector(".navbar .dropdown li:nth-child(2)").click()

    def click_on_navbar_desctop(self):
        driver = self.driver
        click_on_navbar_desctop = driver.find_element_by_css_selector(".navbar .collapse.navbar-collapse li:nth-child(1)").click()

    def open_monitors(self):
        driver = self.driver
        open_monitors = driver.find_element_by_css_selector(".navbar-nav .dropdown.open li:nth-child(3)").click()

    def click_on_navbar_item(self, navbaritem):
        driver = self.driver
        click_on_components = driver.find_element_by_xpath('*//nav//a[contains(text(), "%s")]' % navbaritem).click()
        time.sleep(1)

    def check_cart_click_on_addtocart_iMAC(self, item, iphone1_or_iMac2):
        driver = self.driver
        driver.find_element_by_css_selector('.product-layout:nth-child(%s) button:nth-child(1)' % item).click()
        time.sleep(2)
        driver.find_element_by_css_selector('.container .col-sm-3 #cart').click()
        time.sleep(1)
        if driver.find_element_by_css_selector(
                '.container .row .col-sm-3 #cart .text-center').text == 'Your shopping cart is empty!':
            click_on_addtocart_iMac = driver.find_element_by_css_selector(
                '#content .col-xs-6:nth-child(%s) button:nth-child(1)' % iphone1_or_iMac2).click()
            time.sleep(1)
        else:
            pass

    def click_on_monitors(self):
        driver = self.driver
        click_on_monitors = driver.find_element_by_css_selector(
            '.dropdown.open div:nth-child(2) .list-unstyled li:nth-child(2)').click()
        time.sleep(1)

    def click_on_cameras(self):
        driver = self.driver
        click_on_cameras = driver.find_element_by_css_selector(
            '.container #menu .collapse .nav li:nth-child(7)').click()
        time.sleep(1)


    def click_on_tablets(self):
        driver = self.driver
        click_on_tablets = driver.find_element_by_xpath('*//nav//a[contains(text(), "Tablets")]').click()
        time.sleep(1)


    def click_on_shopping_cart(self):
        driver = self.driver
        click_on_shopping_cart = driver.find_element_by_css_selector('.container .row .col-sm-3 #cart-total').click()
        if driver.find_element_by_css_selector('.container .row .col-sm-3 p').text == 'Your shopping cart is empty!':
            click_on_add_to_cart = driver.find_element_by_css_selector('.row #content div:nth-child(3) button').click()
        else:
            pass










    def destroy(self):
        self.driver.close()






