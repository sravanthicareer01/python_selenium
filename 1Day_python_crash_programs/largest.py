# list1=[10,20,40,50,30,40,50]
# #remove duplicates
# List1_1=list(set(list1))
# print(List1_1)
# sortedlist=sorted(List1_1)
# print(sortedlist)
# print("largest number is:",sortedlist[-1])

#without using reverse index
List1=[10,40,30,50,25,40]
dup_removal= list(set(List1))
print(dup_removal)
print("list without duplicates are:",dup_removal)
largest=dup_removal[0]
smallest=dup_removal[0]
second_largest=dup_removal[0]

for number in dup_removal:
    if number > largest:
        largest=number

print("largest number is:",largest)
for number in dup_removal:
    if number < smallest:
        smallest=number
print("smallest number is :",smallest)





