'''tp6_meter ropa en carrito
Sitio: http://automationpractice.com/index.php
1-Buscar por T-shirts
2-Al elemento que aparece, le clickean el color naranja
3-Poner 25 en cantidad
4-Clickear 3 veces el boton +
5-Verificar que el numero que aparece es 28
'''
import unittest
from selenium import webdriver
import time

class SearchCases(unittest.TestCase):
    
    def test_search_find_tshirts(self):
        driver = webdriver.Chrome('Chromedriver.exe')
        driver.get('http://automationpractice.com/index.php')
        driver.find_element_by_id('search_query_top').send_keys('t-shirts')
        driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="search"]').click()
        time.sleep(2)
        driver.find_element_by_id('color_1').click()
        time.sleep(2)
        driver.find_element_by_name('qty').send_keys('\b')
        driver.find_element_by_name('qty').send_keys(25)
        driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').click()
        driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').click()
        driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').click()
        #  '', 'location', 'location_once_scrolled_into_view', 'parent', 'rect', 'screenshot', 'screenshot_as_base64', 'screenshot_as_png', 'send_keys', 'size', 'submit', 'tag_name', 'text', 'value_of_css_property'
        #print(dir(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i')))
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').id)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').is_displayed)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').is_enabled)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').is_selected)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').parent)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').rect)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').text)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').screenshot)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').size)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').submit)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').send_keys)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').size)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').tag_name)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').text)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').value_of_css_property)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').submit)
        print(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').submit)
        time.sleep(2)
        
        #self.assertEqual(driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').text, '28')
        driver.close()
        driver.quit()

if __name__ == '__main__':
    unittest.main()
