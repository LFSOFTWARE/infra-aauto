from basePage import BasePage
from sheet import Sheet
from login import Login
from entidade import Entidade
from depositante import Depositante

from selenium import webdriver
import time

sheet_class = Sheet("C:/Users/luiz_/workspace/pessoal/infra-auto/infraAuto/silt-template.xlsx")
sheet_data = sheet_class.Import('Entidade')

url_base = "https://synapcomhml2.seniorcloud.com.br/siltwms/"
driver = webdriver.Chrome()
driver.get(url_base)

# Iterar sobre as linhas do DataFrame
for row in sheet_data.itertuples(index=False):
  col1_value = row.fantasia
  col2_value = row.razao_social
  print(row)
  base_page = BasePage(driver);

  login_page = Login(base_page);
  login_page.Login("LUIZ.SSANTOS","Dankicode2002")

  time.sleep(2)

  entidade_page = Entidade(base_page, row)
  # entidade_page.create()
  
  depositante_page = Depositante(base_page, row)
  depositante_page.create()

  time.sleep(30)
