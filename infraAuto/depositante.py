from basePage import BasePage
from interfaces import Empresa
import time


class Depositante:
    def __init__(self, base_page: BasePage, data: Empresa):
        self.base_page = base_page
        self.data = data

    def create(self):
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                          "NavigationView_tree-FolderCadastroEntidade",
                                          "NavigationView_tree-ItemEntidade"], True)
        time.sleep(2)
        
        self.base_page.closeTab()
        time.sleep(2)
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro","NavigationView_tree-ItemDepositante"], True)

        self.base_page.ReturnToMainContext()
        self.base_page.switchToCotext("slickGridFrame")
        time.sleep(10)

        self.base_page.findAndClick("rowNum-0")
        self.base_page.ReturnToMainContext()
        self.base_page.findAndClick("tb-Controle-Duplicardepositante")
        self.base_page.findAndClick("EntidadeSimple_Entidade")
        self.base_page.findAndWrite(self.data.razao_social,"SearchTriggerWindowRemote_searchTextField", pressEnter=True)
        self.base_page.awaitLoad()
        element = self.base_page.findByClass("x-grid3-col-FANTASIA")
        element.click()
        
        time.sleep(2)
        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")
        self.base_page.findAndClick("CadastroWindow_salvarDuplicarcadastrodedepositanteButton")
        print("Create - Depositante")
