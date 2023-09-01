import time

import pytest
import conftest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.carrinho
@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto1 = "Sauce Labs Backpack"
        produto2 = "Sauce Labs Bolt T-Shirt"

        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.adicionarCarrinho("Sauce Labs Backpack")
        time.sleep(2)
        home_page.acessar_carrinho()
        time.sleep(2)
        carrinho_page.verificar_produto_carrinho_existe(produto1)
        time.sleep(2)
        carrinho_page.clicar_continuar_comprando()
        time.sleep(2)
        home_page.adicionarCarrinho(produto2)
        time.sleep(2)
        home_page.acessar_carrinho()
        time.sleep(2)
        carrinho_page.verificar_produto_carrinho_existe(produto1)
        time.sleep(2)
        carrinho_page.verificar_produto_carrinho_existe(produto2)
        time.sleep(2)


