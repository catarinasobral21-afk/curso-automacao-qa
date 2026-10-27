import pytest

@pytest.mark.parametrize("senha", [
    "senha123",
    "abc456",
    "teste999"
])
def test_senhas_invalidas(senha):
    print(senha)