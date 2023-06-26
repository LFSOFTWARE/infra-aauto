from basePage import BasePage
from interfaces import Empresa
from interfaces import SetorI
from interfaces import DataOr
import time


class Or:
    def __init__(self, base_page: BasePage, data: SetorI, data_or: DataOr):
        self.base_page = base_page
        self.data = data
        self.data_or = data_or

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
            if element.text == 'Conf. OR Automática':
                element.click()
                break

        self.base_page.findAndClick("DepositanteConfiguracaoORAutomaticaScreenDescriptor_tipoRecebimento-input")
        
        self.base_page.findAndWrite(self.data_or.codigo_tipo_recebimento,
                                    "SearchTriggerWindowRemote_searchTextField", pressEnter=True)
        
        # self.base_page.teste(self.data_or)
        # self.base_page.inputFormMultiple([
        #     {"id":"DepositanteConfiguracaoORAutomaticaScreenDescriptor_placaVeiculo", "value":"x"},
        #     {"id":"DepositanteConfiguracaoORAutomaticaScreenDescriptor_placaVeiculo", "value":"x"},
        #     {"id":"DepositanteConfiguracaoORAutomaticaScreenDescriptor_placaVeiculo", "value":"x"},

        # ])
