def selection_sort(arr):
    print("\n Selection Sort working steps:")
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
            print(f"Round{i+1}:Samllest element is {arr[min_index]},swapping with {arr[i]}")
            arr[i],arr[min_index]=arr[min_index],arr[i]
            print("Current list:",arr)
    return arr
nums=list(map(int,input("enter elements").split()))
print("\nSelection sort Result :",selection_sort(nums[:]))
