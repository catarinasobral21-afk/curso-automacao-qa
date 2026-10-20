from playwright.sync_api import expect

def test_login_com_sucesso(page):
    # 1. Abrir o site
    page.goto("https://www.saucedemo.com/")

    # 2. Preencher o usuário
    page .locator("#user-name").fill("standard_user")

    # 3. Preencher a senha 
    page .locator("#password").fill("secret_sauce")

    # 4. Clicar no botão de login
    page.locator("#login-button").click()

    # 5. Validar o resultado esperado
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_login_com_senha_invalida(page):
        page.goto("https://www.saucedemo.com/")

        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("senha123")
        page.locator("#login-button").click()

        expect(page.locator("[data-test='error']")).to_be_visible()
