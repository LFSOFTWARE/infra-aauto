import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.time = 120

    def findById(self, id, all=False):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                        EC.presence_of_element_located((By.ID, id))
                    )
            return element
        except Exception as e:
            print("Houve um erro em findById")
       

    def findByClass(self, className, all=False):
        try:
            if all:
                elements = WebDriverWait(self.driver, self.time).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, className))
                )
                return elements

            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.CLASS_NAME, className))
            )
            return element
        except Exception as e:
            print("Houve um erro em findById")
    def findAndWrite(self, value, id, pressEnter=False, pressTab=False):
        try:
            element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
            )
            time.sleep(2)
            try:
                element.clear()
            except ElementNotInteractableException:
                pass
            time.sleep(2)
            element.send_keys(value)

            if pressEnter:
                time.sleep(2)
                element.send_keys(Keys.ENTER)
            if pressTab:
                time.sleep(2)
                element.send_keys(Keys.TAB)

        except Exception as e:
            print("Houve um erro em findById")

    def findAndClick(self, id):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.ID, id))
            )
            element.click()
        except Exception as e:
            print("Houve um erro em findById")
    def closeAll(self):
        try:
            elements = self.finAllByCssSelector("a.x-tab-strip-close", all=True)
            for element in elements:
                try: 
                    element.click()
                except Exception as e:
                    print(f"Ocorreu uma exceção: {type(e).__name__}: {str(e)}")
                time.sleep(2)
        except Exception as e:
            print("Houve um erro em findById")

    def findAndClickByClass(self, id):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.CLASS_NAME, id))
            )
            element.click()
        except Exception as e:
            print("Houve um erro em findById")

    def switchToCotext(self, id):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.ID, id))
            )
            self.driver.switch_to.frame(element)
        except Exception as e:
            print("Houve um erro em findById")

    def ReturnToMainContext(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print("Houve um erro em findById")

    def findAndDoubleClick(self, id):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.ID, id))
            )
            self.actions.double_click(element).perform()
        except Exception as e:
            print("Houve um erro em findById")

    def findAndClickArray(self, ids, isDuble=False):
        try:
            for id in ids:
                element = WebDriverWait(self.driver, self.time).until(
                    EC.presence_of_element_located((By.ID, id))
                )
                if isDuble:
                    self.actions.double_click(element).perform()
                else:
                    element.click()

            time.sleep(2)
        except Exception as e:
            print("Houve um erro em findById")

    def inputFormMultiple(self, data):
        try:
            for obj in data:
                self.findAndWrite(obj['value'], obj['id'])
        except Exception as e:
            print("Houve um erro em findById")

    def findByXpathAndClick(self, xpath, isDuble=False, element="div"):
        try:
            path = f"//{element}[contains(text(), {xpath})]"
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            if isDuble:
                self.actions.double_click(element).perform()
            else:
                element.click()
        except Exception as e:
            print("Houve um erro em findById")

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
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: self.attribute_value_is_false(
                (By.ID, 'DynamicGrid_refresh'), 'aria-disabled'))
        except Exception as e:
            print("Houve um erro em findById")

    def closeTab(self, aba):
        try:
            self.ReturnToMainContext()
            self.findAndClick(aba)
        except Exception as e:
            print("Houve um erro em findById")

    def awaitSave(self, selector, class_name=False):

        for seg in range(0, 60):
            try:
                if class_name:
                    elemento = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, selector)))
                else:
                    elemento = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, selector)))
                print("Waiting for")
            except TimeoutException:
                break

            time.sleep(1)

        print("Terminou")

    def insert_value_integration(self, value):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input.x-form-field.x-form-text[style='width: 268px;']"))

        )
        element.send_keys(value)

    def button_value_integration(self):
        elements = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button.x-btn-text[style='position: relative; width: 69px;']"))

        )
        for element in elements:
            if (element.text == "Ok"):
                time.sleep(5)
                element.click()
                break

    def findAndClickByCss(self, css):
        time.sleep(5)
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css))

        )
        element.click()

    def finAllByCssSelector(self, cssSelector, all=False):
        if all:
            elements = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, cssSelector))
            )

            return elements
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector))
        )
        return element
    
    def teste(self,data):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, "filter-SETOR"))
        ) 

        # Limpar o conteúdo atual do elemento
        self.driver.execute_script("arguments[0].value = '';", element)

        # Escrever o texto no elemento
        self.driver.execute_script("arguments[0].value = arguments[1];", element, data)

        # Pressionar a tecla Enter
        self.driver.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keydown', {key: 'Enter', bubbles: true}));", element)
        time.sleep(8)
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, "rowNum-0"))
        )     
        self.driver.execute_script("arguments[0].click();", element)
        
    def buttonDireito(self):

        elment = self.finAllByCssSelector("td.x-grid3-col.x-grid3-cell.x-grid3-td-SETOR")
        self.actions.context_click(elment).perform()