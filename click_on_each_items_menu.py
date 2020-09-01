def test_00(app):
    app.login_opencart()
    app.click_on_desktops_in_navbar()
    app.click_on_laptops_in_navbar()
    app.click_on_components_in_navbar()
    app.click_on_tablets_in_navbar()
    app.click_on_software_in_navbar()
    app.click_on_phones_pdas_in_navbar()
    app.click_on_cameras_in_navbar()
    app.click_on_mp3_players_in_navbar()
    app.click_on_tablets_in_navbar()
    app.click_on_products()
    app.click_on_add()
    app.click_on_navbar_desctop()
    app.click_on_navbar_dropdown_menu_PC0()

        #assert "There are no products to list in this category." in driver.find_element_by_css_selector("#content p").text

