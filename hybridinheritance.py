class Cal:
    def add(self):
        a=5
        b=6
        print("Addition:", a + b)
class Cal1(Cal):  
    def sub(self):
        a=7
        b=6
        print("Subtraction:", a - b)
class Cal2(Cal):  
    def prod(self):
        a=2
        b=3
        print("Multiplication:", a * b)
class Cal3(Cal1, Cal2):   
    def div(self):
        a=8
        b=2
        print("Division:", a // b)
obj=Cal3()
obj.add()
obj.sub()
obj.prod()
obj.div()
