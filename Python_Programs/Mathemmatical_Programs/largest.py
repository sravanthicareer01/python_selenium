list1=[23,45,34,67,23,45]
list1_1=set(list1)
print(list1_1)
sortedList=sorted(list1_1)
print(sortedList)
largest=sortedList[0]
smallest=sortedList[0]
second_largest=sortedList[0]
for number in sortedList:
    if number>largest:
        second_largest=largest
        largest=number
    elif number>second_largest and number<largest:
        second_largest=number
print("largest number is:",largest)
print("second largest number is:",second_largest)



