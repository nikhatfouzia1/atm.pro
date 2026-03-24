from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class triangle(Shape):
    def area(self):
        print("area of triangle=1/2*b*h")
r=triangle()
r.area()
class Square(Shape):
    def area(self):
        print("area of square=s*s")
S=Square()
S.area()



(i,e.ABC=abstract base Class)
