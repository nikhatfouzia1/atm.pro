arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
if len(arr1) != len(arr2):
    print("Arrays must be of same length")
else:
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
        print("Sum of arrays:", result)


      #OR


arr1=[1,2,3,4]
arr2=[5,6,7,8]
sum_array=[]
for i in range(len(arr1)):
    sum_array.append(arr1[i]+arr2[i])
print("Sum of two arrays:",sum_array)
