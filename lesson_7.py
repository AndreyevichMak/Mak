def test_7(app):
    app.login_opencart()
    app.click_on_mp3player()
    app.click_on_test()

#assert 'There are no products to list in this category.' in driver.find_element_by_css_selector('#content ').text