from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize(
    "usuario, senha, mensagem_esperada",
    [
        ("standard_user", "senha_errada", "Username and password do not match"),
        ("", "secret_sauce", "Username is required")
    ]
)

def test_login_com_diferentes_dados(page, usuario, senha, mensagem_esperada):
    login_page = LoginPage(page)


    login_page.abrir()
    login_page.fazer_login(usuario, senha)
    login_page.validar_mensagem_erro(mensagem_esperada)



def test_login_com_sucesso(page):
    login_page = LoginPage(page)

    login_page.abrir()
    login_page.fazer_login("standard_user", "secret_sauce")
    login_page.validar_login_com_sucesso()

