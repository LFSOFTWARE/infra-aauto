from basePage import BasePage
from interfaces import Empresa
from interfaces import SetorI
from interfaces import PadraoIntegracaoI
import time


class PadraoIntegracao:
    def __init__(self, base_page: BasePage, data: SetorI,  data_padrao: PadraoIntegracaoI, empresa: Empresa):
        self.base_page = base_page
        self.data = data
        self.data_padrao = data_padrao
        self.empresa = empresa

    def create(self):
        time.sleep(2)

        # self.base_page.closeTab("AbaDepositanteClose")
        # self.base_page.closeTab("AbaDanodaOrdemdeRecebimentoClose")

        self.base_page.findAndClickArray(
            ["NavigationView_tree-FolderCadastro", "NavigationView_tree-ItemDepositante"], True)
        self.base_page.switchToCotext("slickGridFrame")

        self.base_page.findAndWrite(
            self.empresa.razao_social.item(), "filter-RAZAOSOCIAL", pressEnter=True)
        
        time.sleep(10)
        
        self.base_page.findAndClick("rowNum-0")
        self.base_page.ReturnToMainContext()
        self.base_page.findAndClickByCss(
            "button.x-btn-text[style='position: relative; width: 12px;']")

        elements = self.base_page.finAllByCssSelector(
            "a.x-menu-item.x-component", all=True)

        time.sleep(10)

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
            if element.text == self.data_padrao.tipo_palete_completo.item():
                element.click()
                break

        # Tipo Alocação Palete Incompleto:
        self.base_page.findAndClick(
            "PadraoIntegracaoRegraNegocioDepositanteScreenDescriptor_tipoAlocacaoPaleteIncompleto")
        elements = self.base_page.finAllByCssSelector(
            "div.x-combo-list-item", all=True)
        for element in elements:
            if element.text == self.data_padrao.tipo_palete_incompleto.item():
                element.click()
                break

         # Tipo Alocação Palete Sobra:
        self.base_page.findAndClick(
            "PadraoIntegracaoRegraNegocioDepositanteScreenDescriptor_tipoAlocacaoPaleteSobra")
        elements = self.base_page.finAllByCssSelector(
            "div.x-combo-list-item", all=True)
        for element in elements:
            if element.text == self.data_padrao.tipo_palete_sobra.item():
                element.click()
                break

        # Tipo Alocação Palete Unidade:
        self.base_page.findAndClick(
            "PadraoIntegracaoRegraNegocioDepositanteScreenDescriptor_tipoAlocacaoPaleteUnidade")
        elements = self.base_page.finAllByCssSelector(
            "div.x-combo-list-item", all=True)
        for element in elements:
            if element.text == self.data_padrao.tipo_palete_unidade.item():
                element.click()
                break
        
        
        if self.data_padrao.ativo.upper() == 'SIM':
            pass
        if self.data_padrao.picking_dinamico.upper() == 'SIM':
            pass
        if self.data_padrao.aceita_qualquer_barra.upper() == 'SIM':
            pass
        if self.data_padrao.percentual_capacidade.upper() == 'SIM':
            pass
        if self.data_padrao.coleta_lote_industria.upper() == 'SIM':
            pass
        if self.data_padrao.coletar_vencimento_lote.upper() == 'SIM':
            pass
      


        self.base_page.findAndWrite(self.data_padrao.quantidade_maxima_picking.item(),
                                    "PadraoIntegracaoRegraNegocioDepositanteScreenDescriptor_qtdeMaxPicking")

        self.base_page.findAndClick(
            "CadastroWindow_salvarPadrãodeIntegraçãodoDepositante-VTEXBRASIL[9002906]Button")
