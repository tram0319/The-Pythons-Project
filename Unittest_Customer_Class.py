import unittest
from Customer_Class import Customer

class TestCustomer(unittest.TestCase):

    def test_constructor(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        result = customer.firstName
        self.assertEqual(result, "Tom")

        result = customer.lastName
        self.assertEqual(result, "Bombadil")

        result = customer.address
        self.assertEqual(result, "123 Mulberry dr")

        result = customer.phoneNumber
        self.assertEqual(result, "(111)111-1111")

        result = customer.email
        self.assertEqual(result, "TB@middleearth.com")

        result = customer.currentRentals
        self.assertEqual(result, ["The Hulk"])

        result = customer.rentalHistory
        self.assertEqual(result, ["The Hulk"])

    def test_addRental_rentalHistory(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        newRental = "The Thing"
        customer.addRental(newRental)

        self.assertEqual(customer.rentalHistory, ["The Hulk", "The Thing"])
    
    def test_addRental_CurrentRentals(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        newRental = "The Thing"
        customer.addRental(newRental)

        self.assertEqual(customer.currentRentals, ["The Hulk", "The Thing"])

    def test_removeRental_try(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Thing", "The Hulk"])
        
        customer.removeRental("The Thing")
        
        self.assertEqual(customer.currentRentals, ["The Hulk"])

    def test_getFirstName(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        
        result = customer.getFirstName()
        self.assertEqual(result, "Tom")

    def test_getLastName(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        
        result = customer.getLastName()
        self.assertEqual(result, "Bombadil")

    def test_getInfo(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        
        result = customer.getInfo()
        self.assertEqual(result, "Address: 123 Mulberry dr / Phone Number: (111)111-1111 / Email Address: TB@middleearth.com")

    def test_getCurrentRentals(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        result = customer.getCurrentRentals()
        self.assertEqual(result, ["The Hulk"])

    def test_getRentalHistory(self):
       customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
       result = customer.getRentalHistory()
       self.assertEqual(result, ["The Hulk"])

    def test_editFirstName(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        newFirstName = "Frodo"
        customer.editFirstName(newFirstName)
        self.assertEqual(customer.firstName, "Frodo")

    def test_editLastName(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        newLastName = "Baggins"
        customer.editLastName(newLastName)
        self.assertEqual(customer.lastName, "Baggins")

    def test_editAddress(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        newAddress = "Hobbiton"
        customer.editAddress(newAddress)
        self.assertEqual(customer.address, "Hobbiton")

    def test_editPhoneNumber(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        newPhoneNumber = "(222)222-2222"
        customer.editPhoneNumber(newPhoneNumber)
        self.assertEqual(customer.phoneNumber, "(222)222-2222")

    def test_editEmail(self):
        customer = Customer("Tom","Bombadil", "123 Mulberry dr", "(111)111-1111",
                      "TB@middleearth.com", ["The Hulk"])
        newEmail = "FB@middleearth.com"
        customer.editEmail(newEmail)
        self.assertEqual(customer.email, "FB@middleearth.com")



if __name__ == '__main__':
    unittest.main()
