def test_1(app):
    app.login_opencart()
    app.click_on_search()
    app.put_apple_to_search()
    app.click_on_categories()
    app.click_on_button_search()



