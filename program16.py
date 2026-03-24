numbers = [10, 5, 8, 20, 15]
numbers.sort()
second_largest=numbers[3]
print("second largest number",second_largest)



l=list(map(int,input("enter").split( )))
print(l)
l=list(set(l))
l.sort()
print(l[-2])
