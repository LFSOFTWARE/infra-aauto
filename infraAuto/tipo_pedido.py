from basePage import BasePage
from interfaces import SetorI
from interfaces import TipoPedidoI
import time


class TipoPedido:
    def __init__(self, base_page: BasePage, data: TipoPedidoI, setor: SetorI):
        self.base_page = base_page
        self.data = data
        self.setor = setor

    def create(self):
        self.base_page.findAndClickArray(
            ["NavigationView_tree-FolderNotaFiscal", "NavigationView_tree-ItemClassificacaoTipodePedido"], isDuble=True)
        self.base_page.findAndClick("tb-Controle-Cadastrar")

        self.base_page.inputFormMultiple([
            {"id": "ClassificacaoTipoPedidoScreenDescriptor_codigoIntegracao",
                "value": self.data.codigo_integracao},
            {"id": "ClassificacaoTipoPedidoScreenDescriptor_descricao",
                "value": self.data.descricao},
        ])

        self.base_page.findAndClick(
            "CadastroWindow_salvarCadastro-ClassificaçãoTipodePedidoButton")
        # self.base_page.awaitSave()

        self.base_page.switchToCotext("slickGridFrame")
        self.base_page.findAndWrite(
            self.data.descricao, "filter-DESCRICAO", pressEnter=True)
        time.sleep(5)
        self.base_page.findAndClick("rowNum-0")
        self.base_page.ReturnToMainContext()

        self.base_page.findAndClick("tb-VincularaClassificacao-Setor")

        time.sleep(5)
        self.base_page.findAndWrite(
            "Descrição", "SiltTransfere_buscarComboBox")

        self.base_page.findAndWrite(
            self.setor.setor_armazenagem, "SiltTransfere_buscarText", pressEnter=True)
        time.sleep(5)

        element = self.base_page.findByClass("x-grid3-col-MARCADO")
        element.click()
        self.base_page.findAndClick("SiltTransfere_fecharButton")

        # elements = self.base_page.findByClass("x-grid3-col-DESCR", all=True)
        # time.sleep(15)

        # for element in elements:
        #     if element.text == "VTEX - FATURAMENTO":
        #         element.click()
        #         break