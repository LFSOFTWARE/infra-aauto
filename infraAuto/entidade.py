from basePage import BasePage


class Entidade:
    def __init__(self, base_page: BasePage):
        self.base_page = base_page

    def create(self):
        self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                                          "NavigationView_tree-FolderCadastroEntidade",
                                          "NavigationView_tree-ItemEntidade"], True)

        self.base_page.findAndClick("tb-Controle-Cadastrar")
        
        self.base_page.inputFormMultiple(
            [
                {"id":"EntidadeDadosScreenDescriptor_razaoSocial", "value": "Razao social"},
                {"id":"EntidadeDadosScreenDescriptor_nomeFantasia", "value": "Razao Fantasia"},

            ]
        )