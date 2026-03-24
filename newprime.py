n=int(input("enter number"))
c=0
print("divisibility of given number")
for i in range(2,n,1):
    if(n%i==0):
        print(i)
        c=c+1
if(c==0):
    print(n,"is prime")
else:
    print(n,"is not prime")
