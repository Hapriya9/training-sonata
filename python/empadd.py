from employee import Employee
from address import Address
address1=Address("banglore",535657)
address2=Address("hyderabad",560051)

emp1=Employee("Hari","priya","Narasaraopet")
emp2=Employee("Hari","priya",[address1,address2])
print(address1.city)
print(address2.pincode)
