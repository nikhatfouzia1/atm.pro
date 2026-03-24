#without function
l=list(map(int,input("values").split()))
Key=int(input("Enter the element:"))
for i in range(0,len(l),1):
    if l[i]==Key:
        print("The",Key,"is in the",i,"index")
        break
else:
        print("The element is not found")

(without function)



#with function
def search_element():
    l=list(map(int,input("Enter values: ").split()))
    key=int(input("Enter the element: "))
    found=False
    for i in range(len(l)):
        if l[i]==key:
            print("The", key, "is in the", i, "index")
            found=True
            break
    else:
            print("The element is not found")
search_element()
                                          


