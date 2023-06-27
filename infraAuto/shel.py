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
while True:
    print("Bem Vindo")
    print("1 - Criar Entidade e suas configurações")
    print("2 - Criar Setor e Depositante")
    print("3 - Criar Tipo recebimento")
    print("1 - Importar Entidade e suas configurações")
    print("1 - Importar Entidade e suas configurações")

    op = int(input(""))

    if op == 1:
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

    elif op == 2:
        sheet_setor = sheet_class.Import('setor')
        for setor in sheet_setor.itertuples(index=False):
            setor = Setor(base_page, setor)
            setor.create()
            setor.createDepositante()

    elif op == 3:
        sheet_setor = sheet_class.Import('tipo_recebimento')
        tipos_recebimento = []

        for tipo in sheet_setor.itertuples(index=False):
            tipos_recebimento.append(tipo.tipo_recebimento)
            setor.tipo_recebimento(tipos_recebimento)
    elif op == 4:
        pass
    elif op == 5:
        pass
    elif op == 6:
        pass
