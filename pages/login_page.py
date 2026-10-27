from playwright.sync_api import expect

class LoginPage:

    def __init__(self, page):
        self.page = page

    def abrir(self):
        self.page.goto("https://www.saucedemo.com/")

    def preencher_usuario(self, usuario):
        self.page.locator("#user-name").fill(usuario)

    def preencher_senha(self, senha):
        self.page.locator("#password").fill(senha)

    def clicar_login(self):
        self.page.locator("#login-button").click()

    def fazer_login(self, usuario, senha):
        self.preencher_usuario(usuario)
        self.preencher_senha(senha)
        self.clicar_login()

    def validar_login_com_sucesso(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )    
        
    def validar_mensagem_erro(self):
        mensagem_erro = self.page.locator("[data-test='error']")
        expect(mensagem_erro).to_be_visible()
        expect(mensagem_erro).to_contain_text(
            "Username and password do not match"
        )    