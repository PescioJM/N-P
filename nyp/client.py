
# -*- coding: utf-8 -*-
#!/usr/bin/env python

# metadata:
__author__ = "Juan Manuel Pescio"
__email__ = "juanmp012@gmail.com"


class Client:
    self.first_name = str(input("Please, enter your first name: "))
    self.last_name =  str(input("Enter your last name: "))
    self.contact = str(input("Enter your phone number: "))
    self.address = str(input("Enter your address: "))
    self.zip = str(input("Enter your ZIP Code: "))
    def __str__(self):
        return (self.first_name,self.last_name,self.contact,self.address,\
self.zip,self.credit)

class Rent:
    self.bikes = input("How many bicycles do you want to rent ?")
    self.mod = input("Please, enter 1 if you want to rent by hour \
, enter 2 if you want to rent by day or enter 3 if you want to rent by week")
    def isFamilyRental():
        if (bikes > 3 and self.bikes < 5):
            var = input("If you want a family promotion enter 1, \
            otherwise enter any other key")
        if var == 1:
            return True
        else:
            return False
    def rent_cost ():
        type = {'1':5, '2':20, '3':60}
        time = input("Enter the amount of time: ")
        if isFamilyRental():
            return "Cost of rent: %s" %((self.bikes*type[self.mod]*time)*0.7)
        else:
            return "Cost of rent: %s" %((self.bikes*type[self.mod]*time))


if __name__ == '__main__':
    client1 = Client()
    rent1 = Rent()
    rent1.isFamilyRental()
    rent1.rent_cost()
