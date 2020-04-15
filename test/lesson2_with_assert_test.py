def test_first_test(app):
    app.login_opencart()
    app.click_on_my_acc()
    app.click_on_register()
    app.pesronal_details( name='Mak', password='Makpvl7')
    app.click_on_button()
    app.click_on_continue()
    app.click_on_my_acc()
    app.click_on_login( mail='makarenkoandrew@mail.ru', password='Makpvl7')
