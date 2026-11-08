list1=[2,3,1,5,4,8,0]
length=len(list1)
print("length of list is:",length)
for i in range(length):
    for j in range(length):
        if list1[i]<list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print("sortedlist is",list1)

