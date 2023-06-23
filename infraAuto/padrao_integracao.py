from basePage import BasePage
from interfaces import Empresa
from interfaces import SetorI
from interfaces import DataOr
import time


class PadraoIntegracao:
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
            if element.text == 'Padrão de Integração':
                element.click()
                break

        self.base_page.findAndClick(
            "CadastroWindow_menuTreePanel-RegrasdeNegocio")

        # Tipo Alocação Palete Completo:
        self.base_page.findAndClick(
            "PadraoIntegracaoRegraNegocioDepositanteScreenDescriptor_tipoAlocacaoPaleteCompleto")
        elements = self.base_page.finAllByCssSelector(
            "div.x-combo-list-item", all=True)
        for element in elements:
            if element.text == '1 - Pulmão Utilizado':
                element.click()
                break

        # Tipo Alocação Palete Incompleto:
        self.base_page.findAndClick("PadraoIntegracaoRegraNegocioDepositanteScreenDescriptor_tipoAlocacaoPaleteIncompleto")
        elements = self.base_page.finAllByCssSelector("div.x-combo-list-item", all=True)
        for element in elements:
            if element.text == '1 - Pulmão Utilizado':
                element.click()
                break
        
         # Tipo Alocação Palete Sobra:
        self.base_page.findAndClick("PadraoIntegracaoRegraNegocioDepositanteScreenDescriptor_tipoAlocacaoPaleteSobra")
        elements = self.base_page.finAllByCssSelector("div.x-combo-list-item", all=True)
        for element in elements:
            if element.text == '1 - Pulmão Utilizado':
                element.click()
                break
        
        # Tipo Alocação Palete Unidade:
        self.base_page.findAndClick("PadraoIntegracaoRegraNegocioDepositanteScreenDescriptor_tipoAlocacaoPaleteUnidade")
        elements = self.base_page.finAllByCssSelector("div.x-combo-list-item", all=True)
        for element in elements:
            if element.text == '1 - Pulmão Utilizado':
                element.click()
                break
        
        self.base_page.findAndWrite("1000","PadraoIntegracaoRegraNegocioDepositanteScreenDescriptor_qtdeMaxPicking")


        self.base_page.findAndClick("CadastroWindow_salvarPadrãodeIntegraçãodoDepositante-VTEXBRASIL[9002906]Button")