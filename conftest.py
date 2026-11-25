from pages.login_page import LoginPage
import os
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    relatorio = resultado.get_result()

    if relatorio.when == "call":
        page = item.funcargs.get("page")

        if page:
            if relatorio.passed:
                pasta = "evidencias/aprovados"
            else:
                pasta = "evidencias/falhas"

            os.makedirs(pasta, exist_ok=True)

            nome_teste = item.name.replace("[", "_").replace("]", "")
            caminho = os.path.join(pasta, f"{nome_teste}.png")

            page.screenshot(path=caminho)
            print(f"\nScreenshot salvo em: {caminho}")


@pytest.fixture
def preparar_navegador(page):
    page.goto("https://www.saucedemo.com/")
    return page


@pytest.fixture
def login_realizado(preparar_navegador):
    login_page = LoginPage(preparar_navegador)
    login_page.fazer_login("standard_user", "secret_sauce")
    return preparar_navegador