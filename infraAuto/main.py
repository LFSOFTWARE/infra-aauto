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

import time

sheet_class = Sheet(
    "C:/Users/luiz_/workspace/pessoal/infra-auto/infraAuto/silt-template.xlsx")

sheet_entidade = sheet_class.Import('entidade')

url_base = "https://synapcomhml2.seniorcloud.com.br/siltwms/"
driver = webdriver.Chrome()
driver.get(url_base)

base_page = BasePage(driver)

login_page = Login(base_page)
login_page.Login("LUIZ.SSANTOS", "Dankicode2002")
time.sleep(2)


def create_setor(base_page, sheet, empresa):
    for setor in sheet.itertuples(index=False):
        print(setor)
        setor = Setor(base_page, setor)
        # setor.create()
        # setor.createDepositante()
        sheet_setor = sheet_class.Import('tipo_recebimento')
        tipos_recebimento = []

        for tipo in sheet_setor.itertuples(index=False):
            tipos_recebimento.append(tipo.tipo_recebimento)
        # setor.tipo_recebimento(tipos_recebimento)
        
        sheet_regiao_armazenagem = sheet_class.Import('regiao_armazenagem')
        for regiao in sheet_regiao_armazenagem.itertuples(index=False):
            setor.regiao_armazenagem(regiao)


def create_entidade(base_page, sheet):
    for empresa in sheet.itertuples(index=False):

        entidade_page = Entidade(base_page, empresa)
        # entidade_page.create()

        depositante_page = Depositante(base_page, empresa)
        # depositante_page.create()

        api_rest = Api(base_page, empresa)
        # api_rest.create()

        sheet_ftp = sheet_class.Import('ftp')
        fpt = Ftp(base_page, empresa, sheet_ftp)
        # fpt.create()

        sheet_setor = sheet_class.Import('setor')
        # create_setor(base_page, sheet_setor, empresa)

        sheet_or = sheet_class.Import('or')
        or_page = Or(base_page, sheet_setor, sheet_or)
        #TODO incomplete
        # or_page.create()

        padrao_integracao_page = PadraoIntegracao(base_page, sheet_setor)
        #TODO adicionar dados
        # padrao_integracao_page.create() 

        setor_padrao_page = SetorPadrao(base_page, sheet_setor)
        #TODO adicionar dados
        setor_padrao_page.create()


        time.sleep(30)


create_entidade(base_page, sheet_entidade)
