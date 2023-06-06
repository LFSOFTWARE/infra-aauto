from basePage import BasePage
from login import Login
from entidade import Entidade

import time

from selenium import webdriver

url_base = "https://synapcomhml2.seniorcloud.com.br/siltwms/"

driver = webdriver.Chrome()
driver.get(url_base)

base_page = BasePage(driver);

login_page = Login(base_page);
login_page.Login("LUIZ.SSANTOS","Dankicode2002")
time.sleep(2)

entidade_page = Entidade(base_page)
# entidade_page.create()

entidade_page.Address()


time.sleep(30)
