def test_4(app):
    app.login_opencart()
    app.click_on_shoppingcart()
    #assert 'Your shopping cart is empty!' in driver.find_element_by_css_selector('#error-not-found .row #content').text



