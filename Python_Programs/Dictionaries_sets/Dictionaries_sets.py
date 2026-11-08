#1--->Remove duplicate elements from an ArrayList (Python list equivalent)
"""
#Method1:
we can take directly apply set on list ,set won't allow duplicates , so it will remove duplicates.

#Method2:
1.Take 2 sets
2.iterate elements through the list
3.segregate all elements in two sets
4.print unique set of elements
"""


#Method1:
list1_1=[10,20,10,30,40,24,26,40,30]
#apply set on list to remove duplicates
rmv_dup=list(set(list1_1))
print("list after removing duplicates by applying set on list:",rmv_dup)
sorted_list1=sorted(rmv_dup)
print("sorted list after removal of duplicates are:",sorted_list1)

#Method2
list1_2=[10,20,10,30,40,24,26,40,30]
unique1=set()
duplicate1=set()
for number1 in list1_2:
    if number1 not in unique1:
        unique1.add(number1)
    else:
        duplicate1.add(number1)
print("unique set of elements after removal of duplicates is:",unique1)
print("Duplicate set of elements after removal of unique elements is:",duplicate1)

#2--->Convert dictionary to list
"""
1.Take a dictionary
2.Take an empty list
3.use for loop iterate through the directory using items()
4.append to the empty list
"""

Dictionary1={"name":"sravanthi","class":"M.Tech","city":"Hyderabad"}
list3=[]
for key,value in Dictionary1.items():
    list3.append([key,value])
print("resultant list is :",list3)

#3--->Sort dictionary keys
"""
1.Take a dictionary
2.take an empty list and filter the keys from the dictionary ad=nd save into the empty list
3.traverse through the list , and follow the regular sorting procedure
"""

Dictionary2={"name":"sravanthi","qual":"M.tech","city":"Hyderabad"}
key_list2=[]
for key in Dictionary2:
    key_list2.append(key)
print("key values are:",key_list2)
for i in range(len(key_list2)):
    for j in range(len(key_list2)-1):
        if key_list2[j]>key_list2[j+1]:
            key_list2[j],key_list2[j+1]=key_list2[j+1],key_list2[j]

print("resultant sorted key list is:",key_list2)









