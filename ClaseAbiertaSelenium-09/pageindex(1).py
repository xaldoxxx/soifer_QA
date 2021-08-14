'''
esta clase se dedica a hacer las interacciones de la pagina principal

a mi constructor le paso el webdriver para q lo siga usando
y los xpath, ids, y demas con los q vaya a interactuar

hacer la busqueda es responsabilidad del pageobject


'''
class PageIndex:
    def __init__(self, my_driver):
        self.query_top = 'search_query_top'
        self.query_button = 'submit_search'
        self.driver = my_driver

    def search(self, item):
        self.driver.find_element_by_id(self.query_top).send_keys(item)
        self.driver.find_element_by_name(self.query_button).click()        
        
