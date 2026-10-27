from pages.login_page import LoginPage


def test_login_com_sucesso(page):
    login_page = LoginPage(page)

    login_page.abrir()
    login_page.fazer_login("standard_user", "secret_sauce")
    login_page.validar_login_com_sucesso()