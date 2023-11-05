class Customer:

  def __init__(self, firstName, lastName, address, phoneNumber, email, currentRentals):
    self.firstName = firstName
    self.lastName = lastName
    self.address = address
    self.phoneNumber = phoneNumber
    self.email = email
    self.currentRentals = currentRentals
    self.rentalHistory = currentRentals

  def getInfo(self):
    return f"Address: {self.address} / Phone Number: {self.phoneNumber} / Email Address: {self.email}"
    # This method can be deleted if we need to get address, phoneNumber, and email separately

  def addRental(self, Video):
    self.currentRentals.append(Video)
    self.rentalHistory.append(Video)

  def removeRental(self, Video):
    try:
      self.currentRentals.remove(Video)
    except:
      print("Video not found in list")

  def getFirstName(self):
    return self.firstName

  def getLastName(self):
    return self.lastName

  def getCurrentRentals(self):
    return self.currentRentals

  def getRentalHistory(self):
    return self.rentalHistory