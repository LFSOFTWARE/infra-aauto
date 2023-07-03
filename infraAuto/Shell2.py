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


class InfraAuto:
    def __init__(self):
        self.sheet_class = Sheet(
            "C:/Users/luiz_/workspace/pessoal/infra-auto/infraAuto/silt-template.xlsx")
        self.base_page = None
        self.setor = None

    def start(self):
        url_base = "https://synapcomhml2.seniorcloud.com.br/siltwms/"
        driver = webdriver.Chrome()
        driver.get(url_base)
        self.base_page = BasePage(driver)

        login_page = Login(self.base_page)
        login_page.Login("LUIZ.SSANTOS", "Dankicode2002")
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
        
        time.sleep(3)
        self.base_page.closeAll()

    def create_setor(self):
        sheet_setor = self.sheet_class.Import('setor')

        for setor_data in sheet_setor.itertuples(index=False):
            self.setor = Setor(self.base_page, setor_data)
            self.setor.create()

        for setor_data in sheet_setor.itertuples(index=False):
            self.setor = Setor(self.base_page, setor_data)
            self.setor.createDepositante()

        time.sleep(10)
        
        for setor_data in sheet_setor.itertuples(index=False):
            self.setor = Setor(self.base_page, setor_data)
            tipos_recebimentos = setor_data.tipo_recebimento.split(";")
            self.setor.tipo_recebimento(tipos_recebimentos)

        time.sleep(3)
        self.base_page.closeAll()

    def create_regiao_armazenagem(self):
        sheet_setor = self.sheet_class.Import('setor')
        for setor_data in sheet_setor.itertuples(index=False):
            setor = Setor(self.base_page, setor_data)
            sheet_regiao_armazenagem = self.sheet_class.Import(
                'regiao_armazenagem')
            
            for regiao in sheet_regiao_armazenagem.itertuples(index=False):
               setor.regiao_armazenagem(regiao)
            
            break
        time.sleep(3)
        self.base_page.closeAll()

    def cretae_or(self):
        sheet_or = self.sheet_class.Import('or')
        sheet_setor = self.sheet_class.Import('setor')
        sheet_entidade = self.sheet_class.Import('entidade')

        or_page = Or(self.base_page, sheet_setor, sheet_or, sheet_entidade)
        or_page.create()
        time.sleep(3)
        self.base_page.closeAll()

    def create_padrao_integracao(self):
        sheet_setor = self.sheet_class.Import('setor')
        sheet_padroa_integracao = self.sheet_class.Import('padrao_integracao')
        sheet_entidade = self.sheet_class.Import('entidade')

        padrao_integracao_page = PadraoIntegracao(
            self.base_page, sheet_setor, sheet_padroa_integracao, sheet_entidade)
        padrao_integracao_page.create()
        time.sleep(3)
        self.base_page.closeAll()

    def create_setor_padrao(self):
        sheet_setor_padrao = self.sheet_class.Import('setor_padrao')
        sheet_empresa = self.sheet_class.Import('entidade')
        setor_padrao_page = SetorPadrao(
            self.base_page, sheet_setor_padrao, sheet_empresa)
        setor_padrao_page.create()
        time.sleep(3)
        self.base_page.closeAll()

    def create_tipo_pedido(self):
        sheet_tipo_pedido = self.sheet_class.Import('tipo_pedido')
        sheet_setor = self.sheet_class.Import('setor')
        tipo_pedido_page = TipoPedido(
            self.base_page, sheet_tipo_pedido, sheet_setor)
        tipo_pedido_page.create()
        time.sleep(3)
        self.base_page.closeAll()

    def run(self):
        while True:
            print("Bem Vindo")
            print("1 - Criar Entidade e suas configurações")
            print("2 - Criar Setor e Depositante")
            print("3 - Criar Regiao Armazenagem")
            print("4 - Criar Or")
            print("5 - Criar Padrão Integração")
            print("6 - Criar Setor Padrão")
            print("7 - Criar Tipo Pedido")

            op = 0

            while True:
                user_input = input(": ")
                try:
                    op = int(user_input)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            if op == 1:
                self.create_entidade()
            elif op == 2:
                self.create_setor()
            elif op == 3:
                self.create_regiao_armazenagem()
            elif op == 4:
                self.cretae_or()
            elif op == 5:
                self.create_padrao_integracao()
            elif op == 6:
                self.create_setor_padrao()
            elif op == 7:
                self.create_tipo_pedido()
            elif op == 0:
                break


infra_auto = InfraAuto()
infra_auto.start()
infra_auto.run()
