list1=[10,20,40,20,40,30,55]
#simply applying set

dup=[]
unique=[]
for number in list1:
    if number in unique:
        dup.append(number)
        unique.remove(number)
    elif number not in dup:
        unique.append(number)
print("unique",unique)
print("duplicates",dup)




