from basePage import BasePage
import time


class Entidade:
    def __init__(self, base_page: BasePage, data):
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

        self.base_page.WriteCNPJ("44.584.470/0001-15",
                                 "EntidadeDadosScreenDescriptor_cgc")
        self.EletronicInvoices()
        self.Parameters()
        self.Address()

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
            if elemento.text == "44.584.470/0001-15":
                elemento.click()
                break
        self.base_page.ReturnToMainContext()

        time.sleep(2)

        self.base_page.findAndClick("tb-VincularaEntidade-Endereco")
        self.base_page.findAndClick("tb-Cadastrar")
        self.base_page.findAndWrite("06807000","EnderecoScreenDescriptor_cep")

        time.sleep(2)

        self.base_page.inputFormMultiple([
             {"id": "EnderecoScreenDescriptor_complemento", "value": "perto da casa"},
            {"id": "EnderecoScreenDescriptor_numero", "value": "123"},
           ])

        self.base_page.findAndClick("EnderecoScreenDescriptor_Entrega")
        self.base_page.findAndClick("EnderecoScreenDescriptor_Cobranca")
        self.base_page.findAndClick("EnderecoScreenDescriptor_Endereco Fiscal")
        self.base_page.findAndClick("EnderecoScreenDescriptor_Impressão")
        self.base_page.findAndClick("CadastroWindow_salvarCadastrodeEndereçoButton")
