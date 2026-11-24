import os
import pytest



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    relatorio = resultado.get_result()


    if relatorio.when == "call" and relatorio.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("evidencias", exist_ok=True)


            nome_teste = item.name.replace("[", "_").replace("]", "")
            caminho = os.path.join("evidencias", f"{nome_teste}.png")


            page.screenshot(path=caminho)
            print(f"\nScreenshot salvo em: {caminho}")