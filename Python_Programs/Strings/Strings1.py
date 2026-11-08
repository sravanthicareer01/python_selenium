#1------>Reverse a string
"""
Method1:to reverse we can directly use string[::-1]
Method2:
========
1.Take a string
2.Take a empty string to store the result
3.pick each character from string using for loop and add that char at the beginning of the empty string,
so that empty string updated with result
4.Print the result string
Method3:
========
we have predefined reversed function to reverse string
"""

# String1="Sravanthi_01"
# #Method1
# print("resultant reverse string",String1[::-1])
# #Method2
# String2="Python Programming Language"
# Result1=""
# for char in String2:
#     Result1=char+Result1
# print("resultant string after reversal is:",(Result1))
# #Method3
# String3="Python Programming"
# Result2 = reversed(String3) #gives object not string, to get string we need to use join
# print("".join(Result2))
#=================================================================================================================
#2------>  Remove all whitespace from a string

"""
Method1:
========
1.To remove white spaces we have strip function, so we can directly apply strip function
2.We have rstrip(). lstrip() to remove white spaces form the string respectively

Method2:
========
1.Take a string with white spaces
2.Iterate through each character in string,space also a character
3.if char==white space we can ignore that using continue
4.then add result=result+char
"""
#Method1:
# String4=" Python Programming"
# String5="Python Programming  "
# String6=" Python Programming "
# #using lstrip
# lstrip_result=String4.lstrip()
# print("After removing left white space is:",lstrip_result)
# print("length before lsprip:",len(String4))
# print("length after lstrip:",len(lstrip_result))
# rstrip_result= String5.rstrip()
# print("before applying rstrip:",len(String5))
# print("after applying restrip",len(rstrip_result))
# print("After removing right white space is:",rstrip_result)
# #want to remove space between python and programming
# remove_spaces=String6.strip()
# print("after removing spaces:",remove_spaces)
# print("remove space between python and programming:",remove_spaces.replace(" ",""))

#Method2:
# String6="Sravanthi python learning"
# Result_string =""
# for char in String6:
#     if char==" ":
#         continue
#     Result_string=Result_string+char
# print("Result string after removing spaces",Result_string)
#===================================================================================================
#3---->Find Duplicate characters in string

# String7="Sravanthi"
# Unique_characters=[]
# Duplicate_characters=[]
# for char in String7:
#     if char in Unique_characters:
#         Duplicate_characters.append(char)
#         Unique_characters.remove(char)
#     else:
#         Unique_characters.append(char)
# print("unique characters are:",Unique_characters)
# print("Duplicate characters are:",Duplicate_characters)
#===================================================================================================
#4--->Check two strings are anagrams
"""
Anagram: Rearrangement of words gives the new word or phrase
Method1:
========
1.Take a string
2.Sorted that string it will gives the list of characters
3.compare original and sorted string
"""
# string8="heart"
# string9="sravanthi"
# string10="earth"
# sort_string8=sorted(string8)
# sort_string9=sorted(string9)
# sort_string10=sorted(string10)
# print(sort_string8)
# print(sort_string9)
# print(sort_string10)
# if sort_string8==sort_string10:
#     print(string8,"and",string10,"both string are anagrams")
# else:
#     print("Not anagrams")
#=========================================================================================================
#5----> Count occurrences of each character in a string
"""
1.take a string and empty dictionary to capture char=occurrence like key=value pair
2.pick each character from string using for loop
3.use if to check it is present in empty dictionary or not
4.if it is present increase count in dictionary value to 1
"""
# String10="sravanthi"
# occurrence_1={}
# for char in String10:
#     if char in occurrence_1:
#         occurrence_1[char]+=1
#     else:
#         occurrence_1[char]=1
# print("occurrence of each character in string is:",occurrence_1)

#6--->Check whether one string is a rotation of another
"""
moving characters from left to right [or] right to left
left rotation: each character from beginning move to end
abcd-> bcda(1st left rotation)->cdab(2nd left rotation)
right rotation: each character from ending to beginning
abcd->dabc(1st right rotation)->cdab(2nd right rotation)
s1=abc
s2=cab
s1+s1=>abcabc=>cab present in s1+s1
#make sure length of both are same
"""
# string11="python"
# string12="npytho" #one left rotation of string11
# """
# I have applied left rotation one time on string11,its gives the string12,
# so here I have to check whether string12 rotation of string11
# """
# if len(string11)==len(string12):
#     print("length of",string11 ,"and",string12,"both are same")
# else:
#     print("lengths are different")
# if len(string11)==len(string12) and string12 in string11+string11:
#     print("string12 is rotation string11")
# else:
#     print("its not a rotation")

#7---> Reverse each word of a string
#8---> Reverse a string while preserving the positions of spaces
# string13="python programming"
# #split sentence into words
# words1=string13.split() #list of words
# print("words in sentence are:",words1)
# result1 = ""
# for word in words1:
#    reverse1=""
#    for char in word:
#        reverse1=char+reverse1
#    result1=result1+reverse1+" "
# print("result:",result1)

#9--->Calculate percentages of uppercase, lowercase, digits and special characters
"""
1.Take a string that contain upper,lower,digits,spl characters
2. we have predefined functions isupper(),islower(),isdigit()
3.pick each characters from string using for, and using if we can compare each character from the string
4.percentage=no.of characters per category/total length of the string
"""
# String11="Sravanthi@123#"
# Upper_case=0
# Lower_case=0
# digits=0
# special1=0
# print("length of the string:",len(String11))
# for char in String11:
#     if char.isupper():
#         Upper_case+=1
#     elif char.islower():
#         Lower_case+=1
#     elif char.isdigit():
#         digits+=1
#     else:
#         special1+=1
# print("length of uppercase:",Upper_case)
# print("length of lowercase:",Lower_case)
# print("length of digits:",digits)
# print("length of spl characters:",special1)
# Uppercase_percentage=(Upper_case/len(String11))*100
# Lowercase_percentage =(Lower_case/len(String11))*100
# digit_percentage=(digits/len(String11))*100
# special_percentage=(special1/len(String11))*100
# print("percentage of Uppercase:",Uppercase_percentage)
# print("percentage of Lowercase:",Lowercase_percentage)
# print("percentage of digits:",digit_percentage)
# print("percentage of spl characters:",special_percentage)

#10---> Find the longest substring without repeating characters
"""
1.Take a string
2.pick each character using for loop
3.under for use if to compare if it is not already present in sub,then add to the substring
4.so we get substring without repeating characters
"""
# String13="Python_programming"
# sub_string=""
# for char in String13:
#     if char not in sub_string:
#         sub_string=sub_string+char
# print("longest substring is:",sub_string)



































