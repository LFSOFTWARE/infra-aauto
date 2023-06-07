from basePage import BasePage
from interfaces import Empresa

import time


class Entidade:
    def __init__(self, base_page: BasePage, data: Empresa):
        self.base_page = base_page
        self.data = data

    def create(self):
        # Acessa Entidade
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                          "NavigationView_tree-FolderCadastroEntidade",
                                          "NavigationView_tree-ItemEntidade"], True)

        # Seleciona o tipo de incrição estadual
        self.base_page.findAndClick("tb-Controle-Cadastrar")
        self.base_page.findAndClickArray(["EntidadeDadosScreenDescriptor_tipoInscricaoEstadual",
                                          "EntidadeDadosScreenDescriptor_tipoInscricaoEstadual-0-CONTRIBUINTEICMS",
                                          ])
        # Define o Tipo
        self.base_page.findAndClick(
            "EntidadeDadosScreenDescriptor_tipoEntidade-input")
        self.base_page.findByXpathAndClick(f"'{self.data.tipo}'", True)

        # Inputs
        self.base_page.inputFormMultiple(
            [
                {"id": "EntidadeDadosScreenDescriptor_razaoSocial",
                    "value": self.data.razao_social},
                {"id": "EntidadeDadosScreenDescriptor_nomeFantasia",
                    "value":  self.data.fantasia},
                {"id": "EntidadeDadosScreenDescriptor_inscricaoEstatual",
                    "value": self.data.inscricao_estadual}
            ]
        )

        self.base_page.WriteCNPJ(self.data.cnpj,
                                 "EntidadeDadosScreenDescriptor_cgc")
        self.EletronicInvoices()
        self.Parameters()
        # self.Address()

    def EletronicInvoices(self):
        self.base_page.findAndClick(
            "CadastroWindow_menuTreePanel-NotaFiscalEletronica")
        self.base_page.findAndClick(
            "EntidadeNfeScreenDescriptor_tipoImpressaoDanfe")
        self.base_page.findAndDoubleClick(
            "EntidadeNfeScreenDescriptor_tipoImpressaoDanfe-1-PDF")

    def Parameters(self):
        self.base_page.findAndClick("CadastroWindow_menuTreePanel-Parametros")
        
        if self.data.emite_nf == 'sim':
            self.base_page.findAndClick(
                "EntidadeParametrosScreenDescriptor_Emite Nota Fiscal")
        self.base_page.findAndClick(
            "CadastroWindow_salvarCadastrodeEntidadeButton")

    def Address(self):
        # Acessa Entidade
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                          "NavigationView_tree-FolderCadastroEntidade",
                                          "NavigationView_tree-ItemEntidade"], True)

        time.sleep(5)

        # Muda para o Iframe
        self.base_page.switchToCotext("slickGridFrame")

        elementos_l7 = self.base_page.findByClass("l7", True)

        # Encontra a empresa que esta sendo cadastrada
        for elemento in elementos_l7:
            if elemento.text == self.data.cnpj:
                elemento.click()
                break
        self.base_page.ReturnToMainContext()

        time.sleep(2)

        self.base_page.findAndClick("tb-VincularaEntidade-Endereco")
        self.base_page.findAndClick("tb-Cadastrar")
        self.base_page.findAndWrite(
            self.data.cep, "EnderecoScreenDescriptor_cep")

        time.sleep(2)

        self.base_page.inputFormMultiple([
            {"id": "EnderecoScreenDescriptor_complemento",
                "value": self.data.complemento},
            {"id": "EnderecoScreenDescriptor_numero", "value": self.data.numero},
        ])

        if self.data.entrega == 'sim':
            self.base_page.findAndClick("EnderecoScreenDescriptor_Entrega")

        if self.data.cobranca == 'sim':
            self.base_page.findAndClick("EnderecoScreenDescriptor_Cobranca")

        if self.data.endereco_fiscal == 'sim':
            self.base_page.findAndClick("EnderecoScreenDescriptor_Endereco Fiscal")

        if self.data.impressao == 'sim':
            self.base_page.findAndClick("EnderecoScreenDescriptor_Impressão")
        
        self.base_page.findAndClick(
            "CadastroWindow_salvarCadastrodeEndereçoButton")