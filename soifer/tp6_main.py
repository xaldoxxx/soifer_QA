'''tp6_meter ropa en carrito
Sitio: http://automationpractice.com/index.php
1-Buscar por T-shirts
2-Al elemento que aparece, le clickean el color naranja
3-Poner 25 en cantidad
4-Clickear 3 veces el boton +
5-Verificar que el numero que aparece es 28

NOTA: no estoy pudiendo TESTEAR el 28 antes de agregar a la canasta...

aldo manfredi
'''
import unittest
from selenium import webdriver
import time

class TshirtsPage():
    def __init__(self, driver):
        self.driver = driver
        self.color = 'color_1'
        self.quantity = 'qty'
        self.touchmore = '//*[@id="quantity_wanted_p"]/a[2]/span/i'
        self.addcest = '//*[@id="add_to_cart"]/button/span'

    def ActTshirts(self, cantidad1, cantidad2):
        self.driver.find_element_by_id(self.color).click()
        self.driver.find_element_by_name(self.quantity).send_keys(cantidad1)
        self.driver.find_element_by_name(self.quantity).send_keys(cantidad2)
        self.driver.find_element_by_xpath(self.touchmore).click()
        self.driver.find_element_by_xpath(self.touchmore).click()
        self.driver.find_element_by_xpath(self.touchmore).click()
        self.driver.find_element_by_xpath(self.addcest).click()
        self.driver.implicitly_wait(10)


class PageIndex():    
    def __init__(self, driver):
        self.query_top = 'search_query_top'
        self.query_button = 'submit_search'
        self.driver = driver
        self.buscaentshirts = TshirtsPage(self.driver)

    def search(self, item):
        self.driver.find_element_by_id(self.query_top).send_keys(item)
        self.driver.find_element_by_name(self.query_button).click()
        self.driver.implicitly_wait(10)
        self.buscaentshirts.ActTshirts('\b', 25)
        time.sleep(2)
        #self.driver.implicitly_wait(10)

        
class SearchCases(unittest.TestCase):
    def setUp(self,):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)        
    
    def test_search_find_tshirts(self,):
        self.indexPage.search('t-shirts')
        self.assertEqual(self.driver.find_element_by_id('layer_cart_product_quantity').text, '28')
        #self.driver.implicitly_wait(10)

    def tearDown(self,):
        self.driver.close()
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()
