from basePage import BasePage
from interfaces import SetorI

import time


class Setor:
    def __init__(self, base_page: BasePage, data: SetorI):
        self.base_page = base_page
        self.data = data

    def create(self):
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                         "NavigationView_tree-FolderCadastroArmazem", "NavigationView_tree-ItemSetor"], True)

        self.base_page.findAndClick("tb-Controle-Cadastrar")

        self.base_page.findAndWrite(
            self.data.setor_armazenagem, "SetorScreenDescriptor_descricao")

        self.base_page.findAndWrite(
            self.data.codigo_integracao, "SetorScreenDescriptor_codigoIntegracao")

        self.base_page.findAndClick("SetorScreenDescriptor_area-input")

        self.base_page.findAndWrite(
            self.data.area_setor, "SearchTriggerWindowRemote_searchTextField")

        self.base_page.pressEnter("SearchTriggerWindowRemote_searchTextField")

        time.sleep(2)
        areas_setores = self.base_page.findByClass(
            "x-grid3-col-AREA", all=True)

        for elemento in areas_setores:
            if elemento.text == self.data.area_setor:
                elemento.click()
                break
        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")

        time.sleep(2)

        self.base_page.findAndClick("SetorScreenDescriptor_tipoSetor-input")
        self.base_page.findAndWrite(
            self.data.tipo_setor, "SearchTriggerWindowRemote_searchTextField")
        self.base_page.pressEnter("SearchTriggerWindowRemote_searchTextField")

        time.sleep(2)

        tipos_setores = self.base_page.findByClass(
            "x-grid3-col-TIPOSETOR", all=True)

        for elemento in tipos_setores:
            if elemento.text == self.data.tipo_setor:
                elemento.click()
                break

        self.base_page.findAndClick("SearchTriggerWindowRemote_selectButton")

        if self.data.permite_expedicao_produto == 'sim':
            self.base_page.findAndClick(
                "SetorScreenDescriptor_Permite Expedicão de Produto")
        if self.data.permite_mais_produto_pulmao == 'sim':
            self.base_page.findAndClick(
                "SetorScreenDescriptor_Permite mais de um produto no pulmão")

        self.base_page.findAndClick(
            "CadastroWindow_salvarCadastrodeSetorButton")
        
        print("Create - Setor")

    def createDepositante(self):
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                         "NavigationView_tree-FolderCadastroArmazem", "NavigationView_tree-ItemSetor"], True)

        self.base_page.switchToCotext("slickGridFrame")

        self.base_page.findAndWrite(
            self.data.setor_armazenagem, "filter-SETOR")
        self.base_page.pressEnter("filter-SETOR")

        time.sleep(2)
        self.base_page.findAndClick("rowNum-0")
        
        self.base_page.ReturnToMainContext()

        self.base_page.findAndClick("tb-VincularaoSetor-Depositantes")
        time.sleep(2)
        self.base_page.findAndClick("SiltTransfere_buscarComboBoxComboArrow")
        time.sleep(2)
        self.base_page.findAndClick("SiltTransfere_buscarComboBox-RAZAOSOCIAL")

        self.base_page.findAndWrite(self.data.razao_social,"SiltTransfere_buscarText", pressEnter=True)
        time.sleep(2)
        self.base_page.findAndClickByClass("x-grid-cell-first")
        time.sleep(3)
        self.base_page.findAndClick("tb-DefinirCodigodeIntegracao")
        time.sleep(3)
        self.base_page.insert_value_integration(self.data.codigo_integracao)
        time.sleep(3)
        self.base_page.button_value_integration()
        time.sleep(3)
        self.base_page.findAndClick("SiltTransfere_fecharButton")
       