def test_9(app):
    app.login_opencart()
    app.click_on_navbar_item('Components')
    app.click_on_monitors()
    app.check_cart_click_on_addtocart_iMAC(item='1', iphone1_or_iMac2='1')