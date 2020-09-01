def test_first(app):
    app.login_opencart()
    app.click_on_cameras()
    app.click_on_sort_by()
    app.click_on_list()
    app.click_on_addtocart_nikonD300()
    app.check_shopping_cart()
    app.check_if_else_item()
