from basePage import BasePage
from interfaces import Empresa
from interfaces import SetorI
from interfaces import DataOr
import time


class SetorPadrao:
    def __init__(self, base_page: BasePage, data: SetorI,):
        self.base_page = base_page
        self.data = data

    def create(self):
        self.base_page.findAndClickArray(
            ["NavigationView_tree-FolderCadastro", "NavigationView_tree-ItemDepositante"], True)
        self.base_page.switchToCotext("slickGridFrame")
        self.base_page.findAndWrite(
            self.data.razao_social, "filter-RAZAOSOCIAL", pressEnter=True)

        time.sleep(2)
        self.base_page.findAndClick("rowNum-0")
        self.base_page.ReturnToMainContext()
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
