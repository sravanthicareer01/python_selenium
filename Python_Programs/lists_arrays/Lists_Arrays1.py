#1---> Check whether two arrays are equal
"""
1.Take two arrays
2.compare length,length not equal, they are not equal
3.else they have equal length, the compare the same index of both arrays
4.if equal,both are equal,else they are not equal
"""


# array1=[10,20,30,40,50]
# array2=[10,20,30,40,60]
# if len(array1)!=len(array2):
#     print("array1,array2 are not equal")
#
# if len(array1)==len(array2):
#     for i in range(len(array1)):
#         if array1[i]==array2[i]:
#             print(array1[i],array2[i] ,"are equal")
#         else:
#             print(array1[i],array2[i],"not equal arrays")

#2---> Find duplicate elements in an array
"""
list1=[10,20,"a","@","#","@","#",20,10,30,40]
Duplicate =[]
for char in list1:
    if list1.count(char)>1 and char not in Duplicate:
        Duplicate.append(char)
print("Duplicates are:",Duplicate)
"""

#3---> Find the second-largest number in an integer array
"""
1.Method1:
==========
1.Take an array and sort that array
2.so second last value is the second largest value from sorted list

Method2:
========
1.Take an array and sort that array
2.intilize largest and second largest to first element of list
3.pick each number from list using for loop,compare number with predefined max value
4.If value is greater than largest value, then the value become largest value
5.and largest value become second largest
6.elif: value>second largest and less than largest then value will be second largest
"""
"""
#Method1:
array1=[20,10,4,6,30,45]
sorted_array1=sorted(array1)
print(sorted_array1)
print("second largest element from the list:",sorted_array1[-2])

#Method2
array2=[20,10,4,6,30,45]
sorted_array2=sorted(array2)
print("sorted array2:",sorted_array2)
largest= sorted_array2[0]
second_largest1=sorted_array2[0]
for number in sorted_array2:
    if number>largest:
        second_largest1 = largest
        largest=number

    elif number>second_largest1 and number<largest:
        second_largest1=number
print("largest number is:",largest) #45
print("second largest number is:",second_largest1) #30
"""
#4---> Find all pairs of elements whose sum equals a given number
"""
1.Take an array and find length
2.traverse element using for loop
3.use another for loop to traverse adjacent element
4.using if sum of these two elements and compare with target sum
5.if this is true then print the two numbers
"""
"""
array3=[2,5,6,4,2,7,8]
target_sum=10
for i in range(len(array3)):
    for j in range(i+1,len(array3)):
        if array3[i]+array3[j]==target_sum:
            print("pair elements that will make sum of pair elements:",array3[i],array3[j])
"""
#5---> Find a continuous subarray whose sum equals a given number
"""
array3=[2,5,6,4,2,7,8]
target_sum=10
for i in range(len(array3)):
    for j in range(i+1,len(array3)):
        for k in range(i+2,len(array3)):
            if array3[i]+array3[j]==target_sum:
                print("pair elements that will make sum of pair elements:",array3[i],array3[j])
            elif array3[i]+array3[j]+array3[k]==target_sum:
                 print("elements are:",array3[i],array3[j],array3[k])
"""
#6--->Find the intersection of two arrays
"""
1.Here intersection means common elements between two arrays
2.Take two arrays and remove duplicates by applying set on lists, since set won't allow duplicates
3.apply intersection between two lists
"""
"""
list_1=[15,30,4,5,4,6,"a","sravanthi"]
list_2=[40,4,20,40,6,"a",10,"sravanthi"]
#remove Duplicates
removed_1=set(list_1)
removed_2=set(list_2)
print("lists after removal of duplicates are:",removed_1,removed_2)
intersection_lists=list(removed_1 and removed_2)
print(intersection_lists) 
"""
#7---> Separate zeros from non-zero elements in an array
"""
1.Take an array or list having elements having both 0's and non zero's and take two lists
2.pick each element using for loop
3.compare using if
4.print two lists
"""
"""
array_5=[0,20,1,0,9,4,0,0]
zero_s=[]
non_zeros=[]
for number in array_5:
    if number == 0:
        zero_s.append(number)
    else:
        non_zeros.append(number)
print("array with zeros:",zero_s)
print("array with non_zeros;",non_zeros)
"""
#8---> Find the missing number in an array
"""
1.Here to find out missing number we need sequence numbers ,lets say n=5
2.using sum of sequential elements is n*(n+1)/2
3.substitute n in formula and calculate expected sum
4.calculate actual sum using sum(array3)
5.difference between these 2 sum's is missing number
"""
"""
array_3=[1,2,3,5] #n=5
sum_1=0
n=5
actual_sum=sum(array_3)
print("Actual sum of elements is:",actual_sum)
expected_sum= n*(n+1)/2
print("expected sum is:",expected_sum)
missing_number=(expected_sum)-(actual_sum)
print("missing_number missing_number is:",missing_number) #4
"""
#9---> Count occurrences of each element in an array
"""
1.Create a list or array
2.create empty dictionary to capture key(element) and value(occurrence)
3.pick each value using for loop,using if ,present in dictionary increment 1 or make it as 1
3.print the resultant dictionary which contain element:occurrence pair values
"""
"""
array_4=[2,3,4,5,3,2,5,5,"ab","bc",5,"bc","ab"]
dictionary_1={}
for element in array_4:
    if element in dictionary_1:
        dictionary_1[element]+=1
    else:
        dictionary_1[element]=1
print("Resultant dictionary with element and occurrences is:",dictionary_1)
"""
#10---> Reverse an array
"""
Method1:
========
1.Take an array
2.use reversed function and reverse an array
Method2:
========
1.Take an array
2.take an empty list to save the reversed array
3.pick each element with for loop and add to the at beginning of the empty list
4.print the list
"""
"""
#Method1
array_6=[10,20,30,40,50]
reversed_array_10=reversed(array_6)
print("reversed array of array_6:",list(reversed_array_10))

#Method2
array_5=[10,20,40,30,60]
reversed_array_1 =[]
reversed_array_2=[]
for number in array_5:
    reversed_array_1=[number]+reversed_array_1
print("reversed resultant array is:",reversed_array_1)
for i in range(len(array_5)):
    reversed_array_2=[array_5[i]]+reversed_array_2
print("reversed array is:",reversed_array_2)
"""






















