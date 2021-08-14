# cada pagina de nuestro sistema va tener su propia clase...
# esta clase hace referencia a la tarea


class PageItem:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.quantity = 'quantity_wanted'
        self.plus = 'icon-plus'

# vamos a poner cantidad
    def enter_quantity(self, quantity):
        self.driver.find_element_by_id(self.quantity).clear()
        self.driver.find_element_by_id(self.quantity).send_keys(quantity)

    def add_elements(self, quantity):
        for i in range(quantity):
            self.driver.find_element_by_class_name(self.plus).click()


# nos devuelve el nro q esta dentro de nuestro cuadro de texto
# el metodo .get_attribute('value')   trae el valor de nuestro cuadro
# .get_attribute sirve para cualquier atributo segun lo q quiera extraer....

    def get_number_of_elements(self,):
        return self.driver.find_element_by_id(self.quantity).get_attribute('value')  
