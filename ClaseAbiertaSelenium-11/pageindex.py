# clase 11
# find_elements devuelve un array de webelement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class PageIndex:
    def __init__(self, my_driver):
        self.query_top = (By.ID, 'search_query_top') 
        self.query_button = (By.NAME, 'submit_search')
        self.driver = my_driver
        self.dresses_link = (By.XPATH, '//*[@title="Dresses"]')   # este xpath es de la pag ppal; vimos q hay 2 elementos q tienen dresses de title

    def search(self, item):
        try:            
            search_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_top)) # retorna un webelement
            search_box.send_keys(item)
            search_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.query_button)) # retorna un webelement
            search_button.click()
        except:
            print('no se encuentra el elemento')


    def click_dresses(self,):
        self.driver.find_elements(*self.dresses_link)[1].click()    # clickea el 2do elemento del array del xpath (hay 2 dresses title en el PO)
