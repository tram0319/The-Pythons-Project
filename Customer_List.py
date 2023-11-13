from Customer_Class import Customer


class Customer_List:

    def __init__(self):
        self.cust_list = []

    def add_cust(self, firstName, lastName, address, phoneNumber, email, currentRentals):
        new_cust = Customer(firstName, lastName, address, phoneNumber, email, currentRentals)
        self.cust_list.append(new_cust)

    def remove_cust(self, firstName, lastName):
        for customer in self.cust_list:
            if customer.firstName == firstName and customer.lastName == lastName:
                self.cust_list.remove(customer)
                return f"Removed {customer.firstName + ' ' + customer.lastName} from the list of customers"
        return f'Customer not found in the list of customers'

    def get_cust(self, firstName, lastName):
        for customer in self.cust_list:
            if customer.firstName == firstName and customer.lastName == lastName:
                return customer
        return f'Customer was not found in the customer list'

    def get_cust_list(self):
        return self.cust_list

    def sort_cust(self, attribute, order='asc'):
        reverse = False if order == 'asc' else True
        self.cust_list.sort(key=lambda x: getattr(x, attribute), reverse=reverse)

