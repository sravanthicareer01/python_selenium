#11--->Remove duplicate elements from an array
"""
Method1:-We can simply apply set on list to remove duplicates
Method2:-
1.Create an array
2.pick each character from array
3.if count>1, then add to duplicate list or array
4.else: add to unique list and print unique list
"""


"""
array_6=[10,20,10,20,30,40,30,50]
removed_dupli= sorted(list(set(array_6)))
print("array6 after removal of duplicates:",removed_dupli)

array_7=[10,20,10,20,30,35,20,30]
duplicate7=[]
unique7=[]
for number in array_7:
    if array_7.count(number)>1:
        duplicate7.append(number)
    else:
        unique7.append(number)
print("Duplicate elements in array are:",set(duplicate7))
print("unique elements in array are:",unique7)
"""
#12---> Remove an element from a list
"""
1.create an array
2.set target one which we want to remove from the list
3.After removing print the resultant list
"""
"""
array_8=[20,30,40,50,60]
remove_target=30
result_list7=[]
for element in array_8:
    if element==remove_target:
        continue
    else:
        result_list7=result_list7+[element]
print("result list after removal of target is:",result_list7)
"""
#13--->Rotate an array
"""
1.Take an array
2.use slicing to pick the required part of the array
3.add the remaining at the end of the array
"""
# array_8=[10,20,30,40,50]
# left_rotate=array_8[2:]+array_8[0:2]
# print("left rotation array:",left_rotate)
# print(array_8[::-1])
#
# #14---> Find the most frequent element in an array
# array_9=[10,20,20,10,10,30]
# dictionary_9={}
# for number9 in array_9:
#     if number9 in dictionary_9:
#         dictionary_9[number9]+=1
#     else:
#         dictionary_9[number9]=1
# print("resultant dictionary with key and values are:",dictionary_9)
# max_value1=0
# max_character=""
# for key,value in dictionary_9.items():
#     if value>max_value1:
#         max_value1=value
#         max_character=key
# print("maximum occurrence of key and value is:",max_value1,max_character)

#15---> Find the union and intersection of multiple arrays
# array_10=[10,20,40,50,60,50,10]
# array_20=[20,30,60]
# #union of array
# dup_10=set(array_10)
# dup_20=set(array_20)
# print("arrays after removing duplicates are:",dup_10,dup_20)
# union_array=sorted(list(dup_10 | dup_20))
# print("result of union is:",union_array)
#
# intersection_array=sorted(list(dup_10 & dup_20))
# print("result of intersection is:",intersection_array)

#16---> Reverse a list
# list_10=[10,20,30,40,50]
# reverse_list =reversed(list_10)
# print("reversed list is:",list(reverse_list))
# #using for loop
# list_20=["a",1,"ab",2,"abc"]
# reversed_list_20=[]
# for item1 in list_20:
#     reversed_list_20=[item1]+reversed_list_20
# print("reversed list is:",reversed_list_20)

#17--->Find contiguous subarrays with a given sum
# array_20=[2,4,6,1,5,10,20]
# sum_20=6
# for i in range(len(array_20)):
#     for j in range(i+1,len(array_20)):
#         if array_20[i]+array_20[j]==sum_20:
#             print("digits that sum is equal to sum of contiguous elements:",array_20[i],array_20[j])

#18---> Find the contiguous subarray with the maximum sum
"""
1.calculate maximum sum
2.then pick each element and compare with that maximum sum, so that we can print the maximum
"""
"""
array_30=[2,5,4,3,7,8]
max_sum=array_30[0]
max_subarray=[]
for i in range(len(array_30)):
    current_sum=0
    for j in range(i,len(array_30)):
        current_sum+=array_30[j]
        if current_sum>max_sum:
            max_sum=current_sum
            max_subarray=array_30[i:j+1]
print("maximum value is:",max_sum)
print("max sub array is:",max_subarray)
"""

#19--->Find the smallest and second-smallest elements in an integer array
"""
Metho1:-
=========
1.Take an array
2.sort that array using sorted function
3.retrive the element based on index 
"""
"""
array_40=[20,10,4,5,6,7]
sorted_40=sorted(array_40)
print(sorted_40)
print("smallest and second smallest element in array are:",sorted_40[0],sorted_40[1])
#Method2:
array_a=[20,10,4,5,6,7]
smallest=array_a[0]
second_smallest=array_a[0]
for number in array_a:
    if number<smallest:
        second_smallest = smallest
        smallest=number
    elif number>smallest and number<second_smallest:
        second_smallest=number
print("smallest number is:",smallest)
print("second smallest is:",second_smallest)
"""

#20---> Merge two unsorted arrays
array1=[20,30,4,1,5]
array2=[4,5,3,2,8]
sorted_1=sorted(array1)
sorted_2=sorted(array2)
print("Arrays after sorting",sorted_1,sorted_2)
merged_arrayy=[]
for number in sorted_1:
    merged_arrayy.append(number)
for number in sorted_2:
    merged_arrayy.append(number)
print("resultant array after merging:",merged_arrayy)
sorted_merged_array=sorted(merged_arrayy)
print("merged array after sorting is:",sorted_merged_array)



























