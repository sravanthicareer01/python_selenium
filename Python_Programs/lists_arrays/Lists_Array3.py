#21--->Merge two unsorted arrays
# array1=[20,30,40,50]
# array2=[10,11,12,13,14,15]
# array3=[10,3,42,5]
# array4=[5,4,2,3,1]
# merged_array2=[]
# #method1: concatenation
# merged_array=array1+array2
# print("Method1:concatenation:array after merging is:",merged_array)
# #Method2:using extend()
# merged_array1=array1.extend(array2)
# print("method2:extend():resultant array after merging:",merged_array)
# print("Before merging:",merged_array2)
#
# #method3:using for loop
# for number in array3:
#     merged_array2.append(number)
#
# for number in array4:
#     merged_array2.append(number)
# print("resultant array after merging using for loops:",merged_array2)


#22---> Merge two arrays into one sorted array without duplicates
# array3=[2,10,5,6,7]
# array4=[4,5,2,3,17]
# merged_array3=array3+array4
# print("array after merging is:",merged_array3)
# merged_array3_sorted=sorted(merged_array3)
# print("sorted of merged_array3 is:",merged_array3_sorted)
# #Method1: apply set on list to remove duplicates
# merged_array3_sorted_dup=list(set(merged_array3_sorted))
# print("merged array after removal of duplicates is:",merged_array3_sorted_dup)
# #method2: we can use to sets to remove duplicates
# merged_array4=[2,3,5,7,8,9,2,5,7,10]
# unique1=[]
# duplicate1=[]
# for number in merged_array4:
#     if number in unique1:
#         duplicate1.append(number)
#         unique1.remove(number)
#     else:
#         unique1.append(number)
# print("unique elements are:",unique1)
# print("duplicate elements are:",duplicate1)

#23---> Sort array elements by frequency
"""
1.Here we have to calculate element(key) frequency(value)
2.Take an array of elements having different occurrences
3.first calculate the occurrences of each element using dictionary
4.sort the elements based on frequency
"""


array5=[5,2,9,1,2,9,2,5,5,5]
frequency_1={}
for number in array5:
    if number in frequency_1:
        frequency_1[number]+=1
    else:
        frequency_1[number]=1
print("frequency of each element in array is:",frequency_1)
#sorted(frequency_1) – sorts the dictionary keys.
#key=frequency_1.get – sorts the keys based on their values (frequencies).
#reverse=False – sorts in ascending order (lowest frequency to highest).
sorted_frequency={}
for number in sorted(frequency_1, key=frequency_1.get, reverse=False):
    sorted_frequency[number]=frequency_1[number]
print("sorted array based on frequency is:",sorted_frequency)

#24--->How to remove an element at specific index from an array?
array1=[10,20,40,5,11,34]
print("array before removal for 2nd index element",array1)
#remove element from 2nd index
array1.pop(2)
print("array after removal of 2nd index element is:",array1)

#25--->How to remove specific element from an array?
array2=[10,20,4,32,65,13]
target_ele=20
print("array2 before removal of target element is:",array2)
array2.remove(target_ele)
print("array2 after removal of target element is:",array2)

#26--->How to remove multiple elements at different indices from an array?
"""
1.Take an array
2.Take another array with the indices number we want to remove
3.iterate through the indices array
4.using del we can remove from the list
"""
List2=[20,1,4,56,35,69]
rm_indices=[1,3,4]
for index in sorted(rm_indices,reverse=True):
    del List2[index]
print("resultant list after removal of targeted indices elements is:",List2)

#27--->How to remove multiple specific elements from an array?
List3=[20,45,67,89,38,37]
target_ele=[20,67,37]
for number in List3:
    if number in target_ele:
        List3.remove(number)
print("resultant list after removal of target elements is:",List3)

#28--->How to remove all occurrences of an element in an array?
"""
1.Create a list
2.set a target element
3.Traverse through the list and if that target shouldn't equal to target element
4.print the resultant list after removal of all occurrences of element
"""
list3=[30,20,21,45,67,89,21,4,21]
target_number=21
resultant_list=[]
for number3 in list3:
    if number3!=target_number:
        resultant_list.append(number3)
print("resultant elements list is:",resultant_list)

#29--->sort an array
array6=[20,10,4,5,3,8]
for i in range(len(array6)):
    for j in range(len(array6)-1):
        if array6[j]>array6[j+1]:
            array6[j],array6[j+1]=array6[j+1],array6[j]
print("resultant list after sorting is:",array6)
















