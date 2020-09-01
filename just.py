def test_001(app):
    app.login_opencart()
    app.click_on_navbar_desctop()
    app.click_on_navbar_dropdown_menu_PC0()
    app.click_on_navbar_desctop()
    app.click_on_navbar_dropdown_menu_PC0()
    app.click_on_navbar_desctop()
    # assert "There are no products to list in this category." in driver.find_element_by_css_selector("#content p").text

