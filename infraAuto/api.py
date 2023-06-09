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
        
        self.base_page.findAndClick("tb-ConfiguracaodeIntegracao-Cadastrar")
        self.base_page.findAndClick("ConfiguracaoIntegracaoEntidadeScreenDescriptor_entidade-input")
        self.base_page.findAndWrite(self.data.razao_social,"SearchTriggerWindowRemote_searchTextField", pressEnter=True)
        time.sleep(2)
        self.base_page.pressEnter("SearchTriggerWindowRemote_searchTextField")
        time.sleep(2)
        self.base_page.findAndClick("x-auto-924")
        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")

        if self.data.integracao_via_servico_rest == 'sim':
            self.base_page.findAndClick("ConfiguracaoIntegracaoEntidadeScreenDescriptor_Integracão via Servico Rest")
            
        self.base_page.findAndClick("ConfiguracaoIntegracaoEntidadeScreenDescriptor_armazem-input")
        time.sleep(2)
        elements = self.base_page.findByClass("x-grid3-col-DESCR", all=True)

        for elemento in elements:
            if elemento.text == self.data.armazem:
                elemento.click()
                break

        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")
        self.base_page.findAndClick("CadastroWindow_salvarCadastroConfiguraçãodeIntegraçãoButton")