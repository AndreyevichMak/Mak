def test_2(app):
    app.login_opencart()
    app.open_cart()
    app.add_product_to_cart_in_case_of_empty_cart()



