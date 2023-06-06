from basePage import BasePage
import time


class Entidade:
    def __init__(self, base_page: BasePage):
        self.base_page = base_page
        
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
        self.base_page.findByXpathAndClick("'DEPOSITANTE'", True)

        # Inputs
        self.base_page.inputFormMultiple(
            [
                {"id": "EntidadeDadosScreenDescriptor_razaoSocial",
                    "value": "Razao socialx"},
                {"id": "EntidadeDadosScreenDescriptor_nomeFantasia",
                    "value": "Razao Fantasiax"},
                {"id": "EntidadeDadosScreenDescriptor_inscricaoEstatual",
                    "value": "estadual"}
            ]
        )
        
        self.base_page.WriteCNPJ("44.584.470/0001-15", "EntidadeDadosScreenDescriptor_cgc")
        self.EletronicInvoices()
        self.Parameters()

    def EletronicInvoices(self):
        self.base_page.findAndClick(
            "CadastroWindow_menuTreePanel-NotaFiscalEletronica")
        self.base_page.findAndClick(
            "EntidadeNfeScreenDescriptor_tipoImpressaoDanfe")
        self.base_page.findAndDoubleClick(
            "EntidadeNfeScreenDescriptor_tipoImpressaoDanfe-1-PDF")

    def Parameters(self):
        self.base_page.findAndClick("CadastroWindow_menuTreePanel-Parametros")
        self.base_page.findAndClick(
            "EntidadeParametrosScreenDescriptor_Emite Nota Fiscal")
        self.base_page.findAndClick("CadastroWindow_salvarCadastrodeEntidadeButton")

    def Address(self):
         # Acessa Entidade
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                          "NavigationView_tree-FolderCadastroEntidade",
                                          "NavigationView_tree-ItemEntidade"], True)
        
        self.base_page.findAndClick("tb-Controle-Cadastrar")
        time.sleep(5)
        self.base_page.findAndClick("x-auto-815")
        self.base_page.findAndDoubleClick("rowNum-0")

