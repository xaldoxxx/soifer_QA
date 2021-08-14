'''
Emepzamos a usar by... y vamos sacando el find_element_by
self.query_top va ser una tupla y le vams a decir q va buscar, siendo un objeto de tipo by


esta clase se dedica a hacer las interacciones de la pagina principal

a mi constructor le paso el webdriver para q lo siga usando
y los xpath, ids, y demas con los q vaya a interactuar

hacer la busqueda es responsabilidad del pageobject

expected_conditions
webdriverwait

'''
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
class PageIndex:
    def __init__(self, my_driver):
        self.query_top = (By.ID, 'search_query_top') # ahora tengo una tupla y no le tengo q decir por que l tiene q andar buscando
        self.query_button = (By.NAME, 'submit_search')
        #self.query_top = 'search_query_top'
        #self.query_button = 'submit_search'
        self.driver = my_driver

    def search(self, item):
        # espera hasta q el elemento exista (until es esperar hasta que)
        # EC.presence_of_elements_located el elemento exista
        # el search_ box tiene un tiempo max de 5 segundos, sino fallo
        search_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_top)) # retorna un webelement
        search_box.send_keys(item)
        # hacemos  lo mesmo con el boton
        search_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.query_button)) # retorna un webelement
        search_button.click()
        #self.driver.find_element(*self.query_top).send_keys(item)   # cuando pasamos una tupla a un metodo hay q poner el *, devulve un webelement
        #self.driver.find_element(*self.query_button).click()
        #self.driver.find_element_by_id(self.query_top).send_keys(item)
        #self.driver.find_element_by_name(self.query_button).click()
        
        
