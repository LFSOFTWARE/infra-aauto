import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.time = 50

    def findById(self, id, all=False):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        return element

    def findByClass(self, className, all=False):
        if all:
            elements = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, className))
            )
            return elements

        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.CLASS_NAME, className))
        )
        return element

    def findAndWrite(self, value, id, pressEnter=False, pressTab=False):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        element.send_keys(value)

        if pressEnter:
            time.sleep(2)
            element.send_keys(Keys.ENTER)
        if pressTab:
            time.sleep(2)
            element.send_keys(Keys.TAB)

    def findAndClick(self, id):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        element.click()

    def switchToCotext(self, id):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        self.driver.switch_to.frame(element)

    def ReturnToMainContext(self):
        self.driver.switch_to.default_content()

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

    def WriteCNPJ(self, value, id):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", element, value)

    def pressEnter(self, id):
        time.sleep(3)
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        element.send_keys(Keys.ENTER)

    def attribute_value_is_false(self, locator, attribute):
        element = self.driver.find_element(*locator)
        return element.get_attribute(attribute) == 'false'

    def awaitLoad(self, timeout=60):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: self.attribute_value_is_false(
            (By.ID, 'DynamicGrid_refresh'), 'aria-disabled'))

    def closeTab(self, aba):
        self.ReturnToMainContext()
        self.findAndClick(aba)

        