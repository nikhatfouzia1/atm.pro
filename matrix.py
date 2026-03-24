Array=[1,2,3,4]
r = int(input("Enter row size: "))
c = int(input("Enter col size: "))
L = []
for i in range(0, r, 1):
    L.append([])
    for j in range(0, c, 1):
        val=int(input(f"Enter element [{i}][{j}]: "))
        L[i].append(val)
print("Matrix is:")
for i in range(r):
    print(L[i])
