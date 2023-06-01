from basePage import BasePage

class Entidade:
    def __init__(self, base_page: BasePage):
        self.base_page = base_page;
    
    def create(self):
      self.base_page.findAndClickArray(["NavigationView_tree-FolderCadastro",
                             "NavigationView_tree-FolderCadastroEntidade",
                              "NavigationView_tree-ItemEntidade", "tb-Controle-Cadastrar"], True)
      
      self.base_page.findAndWrite('xxx', "EntidadeDadosScreenDescriptor_razaoSocial")