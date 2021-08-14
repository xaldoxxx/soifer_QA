from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class PageIndex:
    def __init__(self, my_driver):
        self.query_top = (By.ID, 'search_query_top') 
        self.query_button = (By.NAME, 'submit_search')
        self.driver = my_driver

    def search(self, item):
        try:            
            search_box = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_top)) # retorna un webelement
            search_box.send_keys(item)
            search_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.query_button)) # retorna un webelement
            search_button.click()
        except:
            print('no se encuentra el elemento')
