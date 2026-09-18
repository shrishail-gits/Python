""""Instance methods***

class employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("department",self.department)

e1=employee("Shrishail",25000,"ECE")
e2=employee("Rahul",26000,"CSE")

e1.display()
e2.display()

***Methods with Parameters and return in a Method***

class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def increase_salary(self,amount):
        self.salary=self.salary+amount
    def annual_salary(self):
        return self.salary*12
    def display(self):
        print("Name:",self.name)
        print("salary:",self.salary)
        print("department",self.department)
        print("Annual salary:", e1.annual_salary())
        print("Annual salary:", e2.annual_salary())
e1=Employee("shrishail",25000,"ECE")
e2=Employee("Rahul",26000,"CSE")
e1.increase_salary(5000)
e2.increase_salary(4000)
e1.display()
e2.display()"""




