numbers=[9, 8, 7, 12, 14, 46]
max_num=numbers[0]
min_num=numbers[0]
for n in numbers:
    if n>max_num:
        max_num=n
    if n<min_num:
        min_num=n
second_largest=numbers[0]
for n in numbers:
    if n>second_largest and n!=max_num:
        second_largest=n
print("Maximum:", max_num)
print("Minimum:", min_num)
print("Second Largest:", second_largest)



