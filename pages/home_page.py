from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.tituloPagina = (By.XPATH, "//*[text()='Products']")
        self.itemInventario = (By.XPATH, "//div[@class='inventory_item_name' and contains(text(),'{}')]")
        self.botão_addCarrinho = (By.XPATH, "//*[text()='Add to cart']")
        self.icone_carrinho = (By.XPATH,"//*[@class='shopping_cart_link']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.tituloPagina)

    def adicionarCarrinho(self, nomeItem):
        item = (self.itemInventario[0], self.itemInventario[1].format(nomeItem))
        self.clicar(item)
        self.clicar(self.botão_addCarrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)

