from Customer_Class import Customer
import json
import re


class Customer_List:

    def __init__(self):
        self.cust_list = []
        self.read_cust()

    def read_cust(self):
        with open("customer.json", "r") as f:
            # Load the JSON data from the file
            data = json.load(f)
            # Create a new Video object for each item in the JSON data
            for item in data:
                new_cust = Customer(item['firstName'], item['lastName'], item['address'], item['phoneNumber'],
                                    item['email'],
                                    item['currentRentals'])
                # Add the new Video object to the inventory_list
                self.cust_list.append(new_cust)

    def add_cust(self, firstName, lastName, address, phoneNumber, email, currentRentals):
        if re.match("^[a-zA-Z]+$", firstName) and re.match("^[a-zA-Z ]+$", firstName):
            new_cust = Customer(firstName, lastName, address, phoneNumber, email, currentRentals)
            self.cust_list.append(new_cust)
            return f'Added: {firstName, lastName} to customer.'
        elif not re.match("^[a-zA-Z]+$", firstName):
            return f'First name can only contain letters.'
        elif not re.match("^[a-zA-Z]+$", lastName):
            return f'Last name can only contain letters.'
        elif not phoneNumber.isnumeric():
            return f'Phone number can only contain numbers.'
        else:
            return f'An error occured while adding {firstName, lastName} to customer.'


    def remove_cust(self, firstName, lastName):
        for customer in self.cust_list:
            if customer.firstName.capitalize() == firstName and customer.lastName.capitalize() == lastName:
                self.cust_list.remove(customer)
                return f"Removed {customer.firstName + ' ' + customer.lastName} from the list of customers"
        return f'Customer not found in the list of customers'

    def get_cust(self, firstName, lastName):
        for customer in self.cust_list:
            if customer.firstName == firstName and customer.lastName == lastName:
                return customer
        return f'Customer was not found in the customer list'
    
    def edit_cust_info(self, firstName, lastName, newFirst, newLast, newAddress, newPhone, newEmail):
        for customer in self.cust_list:
            if customer.firstName == firstName and customer.lastName == lastName:
                customer.firstName = newFirst
                customer.lastName = newLast
                customer.address = newAddress
                customer.phoneNumber = newPhone
                customer.email = newEmail
                break
        return f'Customer was not found in the customer list'

    def get_cust_list(self):
        return self.cust_list

    def get_cust_list_by_attribute(self, attribute):
        matching_customers = []
        for customer in self.cust_list:
            if attribute in customer.firstName or attribute in customer.lastName or attribute in customer.email or attribute in customer.address:
                matching_customers.append(customer)
        return matching_customers

    def sort_cust(self, attribute, order='asc'):
        reverse = False if order == 'asc' else True
        self.cust_list.sort(key=lambda x: getattr(x, attribute), reverse=reverse)

    def write_cust(self):
        with open("customer.json", "w") as f:
            # Convert the object to a JSON serializable format
            serializable_list = [video.__dict__ for video in self.cust_list]
            # Write the JSON serializable object to the file
            json.dump(serializable_list, f)

