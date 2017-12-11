def emp(id = 0, name = 'None' , salary = 0):
    print("Id : {}, name : {} and Salary : {}".format(id, name, salary))

# emp(101,'Ram', 15000)
#
emp(id = '101', name='Ram', salary='16000')

emp(id = 102, name='Shyam')

def empAddress(*addr):
    print("Address is :",addr)

empAddress("xyz", "abc", "ijk")
