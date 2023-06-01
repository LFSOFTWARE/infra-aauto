from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions =  ActionChains(driver);

    def findAndWrite(self, value, id):
        element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, id))
            )
        element.send_keys(value)

    def findAndClick(self, id):
        element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, id))
            )
        element.click()

    def findAndDoubleClick(self, id):
        element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, id))
            )
        self.actions.double_click(element).perform()

    def findAndClickArray(self, ids, isDuble=False):
            for id in ids:
                element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, id))
                    )
                if isDuble:
                    self.actions.double_click(element).perform()
                else:
                    element.click()

    def inputFormMultiple(self, data):
        for obj in data:
            self.findAndWrite(obj['value'], obj['id'])



    def findAndClear(self, id):
        pass;

    def findAndSendKeys(self, id, value):
        pass;

    def findAndSelect(self, id, value):
        pass;
