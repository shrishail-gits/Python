class Employee:
    total_employees=0
    def __init__(self,name,age,emp_id,salary):
        self.name=name
        self.age=age
        self.emp_id=emp_id
        self.salary=salary
        Employee.total_employees+=1

        #Instance Method
    def display(self):
            print("Name:",self.name)
            print("Age:",self.age)
            print("emp_id:",self.emp_id)
            print("Salary:",self.salary)
        #class Method
    @classmethod
    def count_employees(cls):
        print("Total employees:",cls.total_employees)

e1=Employee("Shrishail",21,101,30000)
e2=Employee("Praveen",22,102,4000)
e3=Employee("Anil",24,103,45000)

e1.display()
print()
e2.display()
print()
e3.display()
print()
Employee.count_employees()

