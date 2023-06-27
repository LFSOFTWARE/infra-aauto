from basePage import BasePage
from interfaces import SetorI
import time


class SetorPadrao:
    def __init__(self, base_page: BasePage):
        self.base_page = base_page

    def create(self):
        self.base_page.ReturnToMainContext()
        time.sleep(5)
        self.base_page.findAndClickByCss(
            "button.x-btn-text[style='position: relative; width: 12px;']")

        elements = self.base_page.finAllByCssSelector(
            "a.x-menu-item.x-component", all=True)

        for element in elements:
            if element.text == 'Setor Padrão':
                element.click()
                break
        
        time.sleep(5)
        self.base_page.findAndWrite(
            "Setor", "SiltTransfere_buscarComboBox")


        self.base_page.findAndWrite("vtex%","SiltTransfere_buscarText",pressEnter=True)
        time.sleep(5)
        self.base_page.buttonDireito()
        self.base_page.findAndClick("SiltTransfere_GRID_MARCARTUDO")

        time.sleep(5)
        self.base_page.findAndWrite("%DOCA%","SiltTransfere_buscarText",pressEnter=True)
        
        time.sleep(5)
        self.base_page.findAndWrite("%BANCADA%","SiltTransfere_buscarText",pressEnter=True)

        time.sleep(2)
        self.base_page.findAndClick("SiltTransfere_fecharButton")
