import unittest
from selenium import webdriver
import time
from pageindex import PageIndex
from pageitems import PageItems

class SearchCases(unittest.TestCase):

# setUp: metodo q se ejecuta antes de cada test... 
    def setUp(self,):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)

    def test_search_no_elements(self):
        self.indexPage.search('hola')
        time.sleep(2)
        self.assertEqual(self.itemsPage.return_no_elements_text(), 'No results were found for your search "hola"')

    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        #self.driver.find_element_by_id('search_query_top').send_keys('dress')
        #self.driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')
        time.sleep(2)
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_title())

# tearDown metodo q sirve para poscondiciones... q quiero q pase cuando termine uan prueba
# En este caso... q cierre el browser y q mate la sesion
    def tearDown(self,):
        self.driver.close()
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()
