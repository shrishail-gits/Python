class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    @staticmethod
    def validate_dimensions(length,breadth):
        if length>0 and breadth>0:
            return True
        else:
            return False
length=10
breadth=5
if Rectangle.validate_dimensions(length,breadth):
    r1=Rectangle(length,breadth)
    print("Area:",r1.area())
    print("Perimeter:",r1.perimeter())
else:
    print("Invalid dimensions")