from basePage import BasePage
from interfaces import Empresa
import time
class Api:
    def __init__(self, base_page: BasePage, data: Empresa):
        self.base_page = base_page
        self.data = data
    def create(self):
        self.base_page.findAndClickArray(["NavigationView_tree-FolderConfiguracao",
                                          "NavigationView_tree-ItemConfiguracaodeIntegracao"], True)
        
        self.base_page.findAndClick("ConfiguracaoIntegracaoEntidadeScreenDescriptor_entidade-input")
        # self.base_page.findAndClick("tb-ConfiguracaodeIntegracao-Cadastrar")
        # self.base_page.findAndWrite(self.data.razao_social,"SearchTriggerWindowRemote_searchTextField", pressEnter=True)
        # time.sleep(2)
        # self.base_page.findAndClick("x-auto-924")