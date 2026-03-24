class Animal():
    def b(self):
        print("Animal eats food")
class Dog(Animal):
    def b1(self):
        print("Dog barks")
class Puppy(Dog):
    def b2(self):
        print("puppy weeps")
A=Animal()
A.b()
D=Dog()
D.b()
D.b1()
P=Puppy()
P.b()
P.b1()
P.b2()
