from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CarrinhoPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.itemInventario = (By.XPATH, "//div[@class='inventory_item_name' and contains(text(),'{}')]")
        self.botao_continuar_comprando = (By.ID,"continue-shopping")

    def verificar_produto_carrinho_existe(self, nomeItem):
        item = (self.itemInventario[0], self.itemInventario[1].format(nomeItem))
        self.verificar_se_elemento_existe(item)

    def clicar_continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando)
