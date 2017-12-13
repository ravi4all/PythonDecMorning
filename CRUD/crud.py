empList = []
empData = {}

def addEmp():
    empName = input("Enter name of emp : ")
    empAge = int(input("Enter age of emp : "))

    empData['Name'] = empName
    empData['Age'] = empAge

    # empList.append([empName, empAge])
    # print(empList)

    empList.append(empData.copy())
    # print(empList)

    for data in empList:
        print(data)

def readEmp():
    pass

def updateEmp():
    pass

def deleteEmp():
    pass

def sortEmp():
    pass

def searchEmp():
    pass

def saveEmp():
    pass

def loadEmp():
    pass


while True:
    print("""
    1. Add Emp
    2. Read Emp
    3. Update Emp
    4. Delete Emp
    5. Search Emp
    6. Sort Emp
    7. Save Emp
    8. Load Emp
    """)


    todo = {
        "1" : addEmp,
        "2" : readEmp,
        "3" : updateEmp,
        "4" : deleteEmp,
        "5" : searchEmp,
        "6" : sortEmp,
        "7" : saveEmp,
        "8" : loadEmp
    }

    userChoice = input("Enter your choice : ")

    todo.get(userChoice)()
