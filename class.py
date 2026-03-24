class Bike:
    Brand="Burgman"
    Color="Black"
    def speed(self):
        print("The speed of bike is 120kmph")
    def mileage(self):
        print("The mileage of bike is 30km/l")
B1=Bike()
print(B1.Brand)
print(B1.Color)
B1.speed()
B1.mileage()




class Hijab:
    def __init__(self,brand,color="Black"):
        self.brand=brand
        self.color=color
H2=Hijab("cotton","white")
H1=Hijab("chiffon","Black")
print(H1.brand,H1.color)
print(H2.brand,H2.color)
        
