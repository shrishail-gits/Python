class student:
    total_students=0
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
        student.total_students+=1
    #Instance method
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)
    #class method
    @classmethod
    def count_students(cls):
        print("Total_Students:",cls.total_students)
s1=student("Shrishail",21,"HTML")
s2=student("Rahul",22,"CSS")
s3=student("Anil",23,"Python")
s1.display()
s2.display()
s3.display()
print()
student.count_students()
