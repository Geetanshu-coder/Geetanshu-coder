'''Create a sample class named Employee with two attributes id and name
employee :
    id
    name
object initializes id and name dynamically for every Employee object created.

emp = Employee(1, "coder")'''

class employee:
    def __init__(self,id,name):
        self.ID= id
        self.Name= name

    def details(self):
        if self.ID == 1:
            print(" This Employee I'D is of ", self.Name)
        elif self.ID == 456:
            print(" This Employee I'D is of ", self.Name)

    def company(self):
        print(self.Name, "is a root of the company")

emp = employee(1, "coder")
emp.details()
emp.company()

emp.display()
# Deleting the property of object
del emp.id
# Deleting the object itself
try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")