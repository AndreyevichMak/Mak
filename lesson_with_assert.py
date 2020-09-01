def test_002(app):
    app.login_opencart()
    app.click_on_navbar_item('Components')
    app.open_monitors()
#assert "There are no products to list in this category." in driver.find_element_by_css_selector('#content p').text
#assert "open" in driver.find_element_by_css_selector(".navbar-nav .dropdown:nth-child(3)").get_attribute("class")
