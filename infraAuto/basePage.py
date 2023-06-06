from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.time = 50

    def findAndWrite(self, value, id):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        element.send_keys(value)

    def findAndClick(self, id):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        element.click()

    def findAndClickFisrtChild(self, id):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        primeiro_filho = element.find_element(By.CSS_SELECTOR, 'div:first-child')
        primeiro_filho.click()


    def findAndDoubleClick(self, id):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        self.actions.double_click(element).perform()

    def findAndClickArray(self, ids, isDuble=False):
        for id in ids:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.ID, id))
            )
            if isDuble:
                self.actions.double_click(element).perform()
            else:
                element.click()

    def inputFormMultiple(self, data):
        for obj in data:
            self.findAndWrite(obj['value'], obj['id'])

    def findByXpathAndClick(self, xpath, isDuble=False, element="div"):
        path = f"//{element}[contains(text(), {xpath})]"
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        if isDuble:
            self.actions.double_click(element).perform()
        else:
            element.click()

    def selectValue(self, name, value):
        select_element = self.driver.find_element(By.NAME, name)
        select = Select(select_element)
        select.select_by_visible_text(value)

    def WriteCNPJ(self, value, id):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)

    
