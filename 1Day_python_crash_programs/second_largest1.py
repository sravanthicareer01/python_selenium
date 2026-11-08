List1=[10,30,20,60,50]
sorted_list=sorted(List1)
print("sorted list is:",sorted_list)
largest=sorted_list[0]
second_largest = sorted_list[0]
for number in sorted_list:
    if number>largest:
        second_largest=largest
        largest=number
    elif number>second_largest and number<largest:
        second_largest = number

print("largest is",largest)
print("second largest is",second_largest)




