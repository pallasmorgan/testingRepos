#Lab 12
# Morgan Pallas
# here I will create a class named Employee that holds information about the employee
class Employee:
    def name():
        name = input("what is your name? ")
        return name
    def hourlyWage():
        wage = float(input("how much do you make each hour? "))
        return wage
    def department():
        department = input("what is your department? ")
        return department
    def employee(name, wage):
        print(f"{name} is making {wage} dollars per hour")
    def increase(amount, wage):
        if amount > 0:
            #wage += amount
            return True
        else:
            return False
            


def main():
    name = Employee.name()
    wage = Employee.hourlyWage()
    department = Employee.department()
    Employee.employee(name, wage)
    amount = float(input(f"how much is the raise for {name}? "))
    newWage = Employee.increase(amount, wage)
    if newWage == True:
        wage += amount
        print(f"The raise for {name} in {department} is {amount}, their new wage is {wage}")
    else:
        print(f"{name} did nor recieve a raise and their wage is still {wage}")
    
    
