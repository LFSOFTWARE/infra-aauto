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


sheet_class = Sheet(
    "C:/Users/luiz_/workspace/pessoal/infra-auto/infraAuto/silt-template.xlsx")
base_page = None
setor = None

url_base = "https://synapcomhml2.seniorcloud.com.br/siltwms/"
driver = webdriver.Chrome()
driver.get(url_base)
base_page = BasePage(driver)

login_page = Login(base_page)
login_page.Login("LUIZ.SSANTOS", "Dankicode2002")
time.sleep(2)

def create_entidade():
    sheet_entidade = sheet_class.Import('entidade')
    for empresa in sheet_entidade.itertuples(index=False):
        entidade_page = Entidade(base_page, empresa)
        entidade_page.create()

        depositante_page = Depositante(base_page, empresa)
        depositante_page.create()

        api_rest = Api(base_page, empresa)
        api_rest.create()

        sheet_ftp = sheet_class.Import('ftp')
        fpt = Ftp(base_page, empresa, sheet_ftp)
        fpt.create()

def create_setor():
    sheet_setor = sheet_class.Import('setor')

    # for setor_data in sheet_setor.itertuples(index=False):
    #     setor = Setor(base_page, setor_data)
    #     setor.create()

    for setor_data in sheet_setor.itertuples(index=False):
        setor = Setor(base_page, setor_data)
        setor.createDepositante()
    for setor_data in sheet_setor.itertuples(index=False):
        setor = Setor(base_page, setor_data)
        tipos_recebimentos = setor_data.tipo_recebimento.split(";")
        setor.tipo_recebimento(tipos_recebimentos)

def create_regiao_armazenagem():
    if setor is not None:
        sheet_regiao_armazenagem = sheet_class.Import(
            'regiao_armazenagem')
        for regiao in sheet_regiao_armazenagem.itertuples(index=False):
            setor.regiao_armazenagem(regiao)
        print("Create - Regiao Armazenagem")
    else:
        print("Nenhum setor foi criado anteriormente.")

def cretae_or():
    sheet_or = sheet_class.Import('or')
    sheet_setor = sheet_class.Import('setor')
    or_page = Or(base_page, sheet_setor, sheet_or)
    or_page.create()

def create_padrao_integracao():
    sheet_setor = sheet_class.Import('setor')
    sheet_padroa_integracao = sheet_class.Import('padrao_integracao')
    padrao_integracao_page = PadraoIntegracao(
        base_page, sheet_setor, sheet_padroa_integracao)
    padrao_integracao_page.create()

def create_setor_padrao():
    setor_padrao_page = SetorPadrao(base_page)
    setor_padrao_page.create()

def create_tipo_pedido():
    sheet_tipo_pedido = sheet_class.Import('tipo_pedido')
    sheet_setor = sheet_class.Import('setor')
    tipo_pedido_page = TipoPedido(
        base_page, sheet_tipo_pedido, sheet_setor)
    tipo_pedido_page.create()

def run():
    while True:
        print("Bem Vindo")
        print("1 - Criar Entidade e suas configurações")
        print("2 - Criar Setor e Depositante")
        print("3 - Criar Regiao Armazenagem")
        print("4 - Criar Or")
        print("5 - Criar Padrão Integração")
        print("6 - Criar Setor Padrão")
        print("7 - Criar Tipo Pedido")

        user_input = input("Enter a number: ")
        op = 0

        try:
            op = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        
        if op == 1:
            create_entidade()
        elif op == 2:
            create_setor()
        elif op == 3:
            create_regiao_armazenagem()
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            create_tipo_pedido()

run()
