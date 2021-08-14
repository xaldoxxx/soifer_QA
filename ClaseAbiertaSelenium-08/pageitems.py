'''
pagina a donde yo voy, la pagina q tiene los items
de donde obtengo los resultados
aparece un banner cuando no tengo resultados, hay un xpath
aparece otro banner si es q hay resultados, otro xpath

'''
class PageItems:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.no_results_banner = '//*[@id="center_column"]/p'
        self.title_banner = '//*[@id="center_column"]/h1/span[1]'

    def return_no_elements_text(self,):
        return self.driver.find_element_by_xpath(self.no_results_banner).text
        
    def return_section_title(self,):
        return self.driver.find_element_by_xpath(self.title_banner).text
        

        
