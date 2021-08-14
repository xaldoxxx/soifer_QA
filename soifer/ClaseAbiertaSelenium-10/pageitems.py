# clase10
# trabajamos sobre el dropbox seleccionando sobre un texto visible, mejoramos trabanjo con By

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # para los select tenemos q importar esta libreria (del select_by_text)

class PageItems:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.no_results_banner = '//*[@id="center_column"]/p'
        self.title_banner = '//*[@id="center_column"]/h1/span[1]'
        self.orange_button = 'color_1'
        self.order = (By.ID, 'selectProductSort')

    def return_no_elements_text(self,):
        return self.driver.find_element_by_xpath(self.no_results_banner).text
        
    def return_section_title(self,):
        return self.driver.find_element_by_xpath(self.title_banner).text

    def click_orange_button(self,):
        self.driver.find_element_by_id(self.orange_button).click()

    def select_by_text(self, text):  #por el texto buscamos
        # metodo q busca texto dentro del drop
        order = Select(self.driver.find_element(*self.order))    # (* para q pueda leer la tupla necesita * delante)  order es una variable local a este metodo, y self.order es una variable global a la clase
        order.select_by_visible_text(text) # seleccioname por un texto visible en el drop... y vamos al test

    def select_by_value(self, value):  #por el texto buscamos
        # metodo q busca por valor dentro del drop
        order = Select(self.driver.find_element(*self.order))    # (* para q pueda leer la tupla necesita * delante)  order es una variable local a este metodo, y self.order es una variable global a la clase
        order.select_by_value(value)

    def select_by_index(self, number):
        order = Select(self.driver.find_element(*self.order))    # (* para q pueda leer la tupla necesita * delante)  order es una variable local a este metodo, y self.order es una variable global a la clase
        order.select_by_index(number)
