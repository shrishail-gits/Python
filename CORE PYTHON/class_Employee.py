class Employee:
    company_name="ABC Company"
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    #Instance method
    def display(self):
        print("Name:",self.name)
        print("ID:",self.emp_id)
        print("Salary:",self.salary)
        print("Company:",Employee.company_name)
    #Class method
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
    #Static method
    @staticmethod
    def validate_salary(salary):
        if salary>0:
            return True
        else:
            return False
e1=Employee("Shrishail",101,30000)
e1.display()
print("Salary valid:",Employee.validate_salary(30000))
Employee.change_company("Dhee Code Lab")
e1.display()
