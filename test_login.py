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

        mensagem_erro = page.locator("[data-test='error']")
        expect(mensagem_erro).to_be_visible()
        expect(mensagem_erro).to_contain_text("Username and password do not match")


def test_login_sem_senha(page):
      page.goto("https://www.saucedemo.com/")

      page.locator("#user-name").fill("standard_user")
      page.locator("#login-button").click()

      mensagem_erro = page.locator("[data-test='error']")
      expect(mensagem_erro).to_be_visible()
      expect(mensagem_erro).to_contain_text("Password is required")

def validar_mensagem_erro(self):
        mensagem_erro = self.page.locator("[data-test='error']")
        expect(mensagem_erro).to_be_visible()
        expect(mensagem_erro).to_contain_text(
            "Username and password do not match"
        )