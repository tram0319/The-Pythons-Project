import unittest
import Customer_List_Class

class TestCustomerList(unittest.TestCase):
    
    def test_constructor(self):
        customers = Customer_List_Class.Customer_List()
        self.assertEqual(len(customers.cust_list), 0)
            
    def test_get_cust_list(self):
        customers = Customer_List_Class.Customer_List()
        self.assertEqual(len(customers.get_cust_list()), 0)
    
    def test_add_cust(self):
        customers = Customer_List_Class.Customer_List()
        customers.add_cust("John", "Doe", "123 Drive", "123-456-7890", "test@gmail.com", 1)
        self.assertEqual(len(customers.get_cust_list()), 1)
        
    def test_remove_cust(self):
        customers = Customer_List_Class.Customer_List()
        customers.add_cust("John", "Doe", "123 Drive", "123-456-7890", "test@gmail.com", 1)
        customers.remove_cust("John", "Doe")
        self.assertEqual(len(customers.get_cust_list()), 0)
        
    def test_get_cust(self):
        customers = Customer_List_Class.Customer_List()
        customers.add_cust("John", "Doe", "123 Drive", "123-456-7890", "test@gmail.com", 1)
        self.assertEqual(customers.get_cust("John", "Doe"), customers.get_cust_list()[0])
        
    def test_get_cust_list_by_attribute(self):
        customers = Customer_List_Class.Customer_List()
        customers.add_cust("John", "Doe", "123 Drive", "123-456-7890", "test@gmail.com", 1)
        customers.add_cust("Jane", "Doe", "123 Lane", "987-654-3210", "test2@gmail.com", 1)
        filteredList = customers.get_cust_list_by_attribute("123 Lane")
        self.assertEqual(filteredList[0].firstName, "Jane")
        
    def test_sort_cust(self):
        customers = Customer_List_Class.Customer_List()
        customers.add_cust("John", "Doe", "123 Drive", "123-456-7890", "test@gmail.com", 1)
        customers.add_cust("Jane", "Doe", "123 Lane", "987-654-3210", "test2@gmail.com", 1)
        customers.sort_cust("firstName", "asc")
        self.assertEqual(customers.cust_list[0].firstName, "Jane")
        
        
if __name__ == '__main__':
    unittest.main()
