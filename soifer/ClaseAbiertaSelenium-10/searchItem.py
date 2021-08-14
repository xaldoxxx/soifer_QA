# clase 10
# mejoramos eñ pageindex con try except
# trabajamos sobre el dropbox en pageitems; haciendo un select por texto, por valor y por indice
import unittest
from selenium import webdriver
import time
from pageindex import PageIndex
from pageitems import PageItems
from pageitem import PageItem     # el page objetct de la tarea


class SearchCases(unittest.TestCase):

    def setUp(self,):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        # paso el webdriver a los page objects
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.itemPage = PageItem(self.driver)

    @unittest.skip('no nexesario')
    def test_search_no_elements(self):
        self.indexPage.search('hola')
        self.assertEqual(self.itemsPage.return_no_elements_text(), 'No results were found for your search "hola"')

    @unittest.skip('no nexesario')
    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    @unittest.skip('no nexesario')
    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_title())

    @unittest.skip('no nexesario')
    def test_tarea(self):
        self.indexPage.search('t-shirt')      # busco tshirt  
        self.itemsPage.click_orange_button()    # click en boton naranja
        self.itemPage.enter_quantity('25')    # pongo 25
        self.itemPage.add_elements(3)     # agrego 3 elementos
        number = self.itemPage.get_number_of_elements()   # number, retorna valor de celda
        self.assertTrue(number == '28')   # testea si la cantidad es 28

    def test_selections(self,):
        self.indexPage.search('t-shirt')      # busco tshirt
        self.itemsPage.select_by_text('Product Name: Z to A')  # busco este texto en el drop; select por texto
        time.sleep(5)
        self.itemsPage.select_by_value('name:asc') # select por valor
        time.sleep(5)
        self.itemsPage.select_by_index(2) # select por indice
        time.sleep(5)
        

        
    def tearDown(self,):
        self.driver.close()
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()
