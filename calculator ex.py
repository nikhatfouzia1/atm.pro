from abc import ABC, abstractmethod
class Calci(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
    @abstractmethod
    def prod(self):
        pass
    @abstractmethod
    def div(self):
        pass
    @abstractmethod
    def mod(self):
        pass
    @abstractmethod
    def expo(self):
        pass
class Cal(Calci):
    def __init__(self):
        self.a=5
        self.b=2
    def add(self):
        print("Addition:", self.a + self.b)
    def sub(self):
        print("Subtraction:", self.a - self.b)
    def prod(self):
        print("Multiplication:", self.a * self.b)
    def div(self):
        print("Division:", self.a // self.b)
    def mod(self):
        print("Remainder:",self.a % self.b)
    def expo(self):
        print("Power:",self.a ** self.b)
s=Cal()
while True:
    print("\n=====CAL MENU=====")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponential")
    print("7. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        s.add()
    elif choice==2:
        s.sub()
    elif choice==3:
        s.prod()
    elif choice==4:
        s.div()
    elif choice==5:
        s.mod()
    elif choice==6:
        s.expo()
    elif choice==7:
        print("Thankyou for using calculator")
        break
    
    else:
        print("Invalid option")
    





        
        








