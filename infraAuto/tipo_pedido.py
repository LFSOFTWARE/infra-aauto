from basePage import BasePage
from interfaces import SetorI
import time
class TipoPedido:
    def __init__(self, base_page: BasePage):
        self.base_page = base_page
        # self.data = data

    def create(self):
        self.base_page.findAndClickArray(["NavigationView_tree-FolderNotaFiscal", "NavigationView_tree-ItemClassificacaoTipodePedido"], isDuble=True)
        self.base_page.findAndClick("tb-Controle-Cadastrar")

        self.base_page.inputFormMultiple([
            {"id":"ClassificacaoTipoPedidoScreenDescriptor_codigoIntegracao","value":"x"},
            {"id":"ClassificacaoTipoPedidoScreenDescriptor_descricao","value":"x"},
        ])


        self.base_page.findAndClick("CadastroWindow_salvarCadastro-ClassificaçãoTipodePedidoButton")

        
        self.base_page.switchToCotext("slickGridFrame")

        self.base_page.findAndWrite("x","filter-DESCRICAO", pressEnter=True)
        time.sleep(5)
        self.base_page.findAndClick("rowNum-0")
        self.base_page.ReturnToMainContext()

        self.base_page.findAndClick("tb-VincularaClassificacao-Setor")
