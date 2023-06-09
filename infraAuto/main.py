from basePage import BasePage
from sheet import Sheet
from login import Login
from entidade import Entidade
from depositante import Depositante
from api import Api
from setor import Setor

from selenium import webdriver
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


def create_entidade(base_page, sheet):
    # Iterar sobre as linhas do DataFrame
    for row in sheet.itertuples(index=False):
        col1_value = row.fantasia
        col2_value = row.razao_social
        entidade_page = Entidade(base_page, row)
        # entidade_page.create()

        depositante_page = Depositante(base_page, row)
        # depositante_page.create()

        api_rest = Api(base_page, row)
        # api_rest.create()


def create_setor(base_page, sheet):
    # Iterar sobre as linhas do DataFrame
    for row in sheet.itertuples(index=False):
        print(row)
        setor = Setor(base_page, row)
        setor.createDepositante()

create_entidade(base_page, sheet_entidade)
time.sleep(5)

sheet_setor = sheet_class.Import('setor')
create_setor(base_page, sheet_setor)

time.sleep(30)
