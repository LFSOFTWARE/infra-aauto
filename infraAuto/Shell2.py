from basePage import BasePage
from sheet import Sheet
from login import Login
from entidade import Entidade
from depositante import Depositante
from api import Api
from setor import Setor
from ftp import Ftp
from selenium import webdriver
from orPy import Or
from padrao_integracao import PadraoIntegracao
from setor_padrao import SetorPadrao
from tipo_pedido import TipoPedido
from interfaces import SetorI

import time
from typing import Optional

class InfraAuto:
    def __init__(self):
        self.sheet_class = Sheet(
            "C:/Users/luiz_/workspace/pessoal/infra-auto/infraAuto/silt-template.xlsx")
        self.base_page = None
        self.setor = None

    def start(self):
        url_base = "https://wms.synapcom.com.br/siltwms/"
        driver = webdriver.Chrome()
        driver.get(url_base)
        self.base_page = BasePage(driver)

        login_page = Login(self.base_page)
        login_page.Login("luiz.ssantos", "Dankicode2002")
        time.sleep(2)

    def create_entidade(self):
        sheet_entidade = self.sheet_class.Import('entidade')
        for empresa in sheet_entidade.itertuples(index=False):
            entidade_page = Entidade(self.base_page, empresa)
            entidade_page.create()

            depositante_page = Depositante(self.base_page, empresa)
            depositante_page.create()

            api_rest = Api(self.base_page, empresa)
            api_rest.create()

            sheet_ftp = self.sheet_class.Import('ftp')
            fpt = Ftp(self.base_page, empresa, sheet_ftp)
            fpt.create()

    def create_setor(self):
        sheet_setor = self.sheet_class.Import('setor')
        for setor_data in sheet_setor.itertuples(index=False):
            print(sheet_setor)
            
        for setor_data in sheet_setor.itertuples(index=False):
            self.setor = Setor(self.base_page, setor_data)
            self.setor.create()
            self.setor.createDepositante()
            tipos_recebimentos =  setor_data.tipo_recebimento.split(";")
            for tipo_recebimento in tipos_recebimentos:
                self.setor.tipo_recebimento(tipo_recebimento)
            
   
    def create_regiao_armazenagem(self):
        if self.setor is not None:
            sheet_regiao_armazenagem = self.sheet_class.Import('regiao_armazenagem')
            for regiao in sheet_regiao_armazenagem.itertuples(index=False):
                self.setor.regiao_armazenagem(regiao)
            print("Create - Regiao Armazenagem")
        else:
            print("Nenhum setor foi criado anteriormente.")
    def run(self):
        while True:
            print("Bem Vindo")
            print("1 - Criar Entidade e suas configurações")
            print("2 - Criar Setor e Depositante")
            print("4 - Criar Regiao Armazenagem")
            print("5 - Importar Entidade e suas configurações")
            print("6 - Importar Entidade e suas configurações")
            print("7 - Importar Entidade e suas configurações")
            print("8 - Importar Entidade e suas configurações")

            op = int(input(""))

            if op == 1:
                self.create_entidade()
            elif op == 2:
                self.create_setor()
            elif op == 3:
                pass
            elif op == 4:
                self.create_regiao_armazenagem()
            elif op == 5:
                pass
            elif op == 6:
                pass
            elif op == 7:
                pass
            elif op == 8:
                pass
            elif op == 9:
                pass
            elif op == 10:
                pass

infra_auto = InfraAuto()
infra_auto.start()
infra_auto.run()
