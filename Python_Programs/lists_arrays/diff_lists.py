list1=[10,20,30,40,5]
list2=[30,20,5]
diff=[]
#diff =[10,40]
for num in list1:
    if num not in list2:
        diff.append(num)
print("difference list",diff)
