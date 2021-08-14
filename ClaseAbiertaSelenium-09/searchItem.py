import unittest
from selenium import webdriver
import time
from pageindex import PageIndex
from pageitems import PageItems
from pageitem import PageItem     # el page objetct de la tarea


class SearchCases(unittest.TestCase):

# setUp: metodo q se ejecuta antes de cada test... 
    def setUp(self,):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(10) # doy 5 segundo a q cargue y puedo sacar todos los time,sleep.. si hace mas de 5 segundos falla la prueba
        # paso el webdriver a los page objects
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.itemPage = PageItem(self.driver)

    @unittest.skip('no nexesario')
    def test_search_no_elements(self):
        self.indexPage.search('hola')
        #time.sleep(2)
        self.assertEqual(self.itemsPage.return_no_elements_text(), 'No results were found for your search "hola"')

    @unittest.skip('no nexesario')
    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        #self.driver.find_element_by_id('search_query_top').send_keys('dress')
        #self.driver.find_element_by_name('submit_search').click()
        #time.sleep(2)
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    @unittest.skip('no nexesario')
    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')
        #time.sleep(2)
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_title())

    def test_tarea(self):
        self.indexPage.search('t-shirt')      # busco tshirt  
        self.itemsPage.click_orange_button()    # click en boton naranja
        self.itemPage.enter_quantity('25')    # pongo 25
        self.itemPage.add_elements(3)     # agrego 3 elementos
        number = self.itemPage.get_number_of_elements()   # number, retorna valor de celda
        self.assertTrue(number == '28')   # testea si la cantidad es 28
        

# tearDown metodo q sirve para poscondiciones... q quiero q pase cuando termine uan prueba
# En este caso... q cierre el browser y q mate la sesion
    def tearDown(self,):
        self.driver.close()
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()
