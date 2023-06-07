from basePage import BasePage
from interfaces import Empresa

class Api:
    def __init__(self, base_page: BasePage, data: Empresa):
        self.base_page = base_page
        self.data = data
    def create(self):
        self.base_page.findAndClickArray(["NavigationView_tree-FolderConfiguracao",
                                          "NavigationView_tree-ItemConfiguracaodeIntegracao"], True)