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
