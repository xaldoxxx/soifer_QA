class PageItem:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.quantity = 'quantity_wanted'
        self.plus = 'icon-plus'
        

    def enter_quantity(self, quantity):
        self.driver.find_element_by_id(self.quantity).clear()
        self.driver.find_element_by_id(self.quantity).send_keys(quantity)

    def add_elements(self, quantity):
        for i in range(quantity):
            self.driver.find_element_by_class_name(self.plus).click()

    def get_number_of_elements(self,):
        return self.driver.find_element_by_id(self.quantity).get_attribute('value')

