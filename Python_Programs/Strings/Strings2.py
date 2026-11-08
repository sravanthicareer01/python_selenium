#11--->Find the first repeated and non-repeated characters in a string
"""
1.Take a string
2.pick each character using for,using if under if count>0,then break else count==1,break
"""


# String15="sravanthiii"
# for char in String15:
#     if String15.count(char)>1:
#         print("first repeated character is:",char)
#         break
# for char in String15:
#     if String15.count(char)==1:
#         print("first non repeated character is:",char)
#         break

#12--->Convert a string to an integer and an integer to a string
# string20="12345"
# str1_num1=int(string20)
# print("string to integer is:",int(string20))
# print(type(str1_num1))
#
# num20=98765
# num1_str1=str(num20)
# print("number to string is:",str(num20))
# print(type(num1_str1))

#13--->Reverse a sentence word by word
# sentence5="This is python programming"
# words5=sentence5.split()
# print("words from the sentence are:",words5)
# result_sentence=""
# for word in words5:
#     reverse_word=""
#     for char in word:
#         reverse_word=char+reverse_word
#     print(reverse_word)
#     result_sentence=result_sentence+reverse_word+" "
# print("reverse sentence word by word:",result_sentence)

#14---> Remove all vowels from a string
"""
# 1.take a string
# 2.create vowel list AEIOUaeiou
# 3.pick each character and compare with vowels list, if it is present we can skip that step
# 4.print the resultant string after vowels removal
# """
# String15="Sravanthi"
# vowels5="AEIOUaeiou"
# vowel_removal=""
# List_vowels=list(vowels5)
# print("vowels list is:",List_vowels) #['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
# for char in String15:
#     if char in List_vowels:
#         continue
#     else:
#         vowel_removal=vowel_removal+char
# print(String15,"after removing vowels is:",vowel_removal)

#15---> Print all substrings of a string
"""
1.Take a string
2.Use the outer for loop to select the starting index.
3.Use the inner for loop to select the ending index.
4.Use string slicing String[i:j] to print each substring.
"""
String_sub="abc"
for i in range(len(String_sub)):
    for j in range(i+1,len(String_sub)+1):
      print(String_sub[i:j])

#16---> Find common characters between two strings in alphabetical order
"""
Method1
========
1.Take strings
2.make list from strings
3.remove duplicates from list by applying set
4.use 'and' between two lists
Method2
========
1.Take two strings
2.pick each character from string1 using for loop as outer loop
3.pick each character from string2 using for loop as inner loop
4.compare characters from each loop ,if match capture that character
"""
#Method1
# String10="sravanthi"
# String20="sravani"
# list10=list(String10)
# print("list of String10:",list10)
# list20=list(String20)
# print("list of String20:",list20)
# set10=set(list10)
# set20=set(list20)
# print("removed duplicates:",set10,set20)
# common_characters=    list(set(list10) and set(list20))
# print(common_characters)
# common_character_sorted=sorted(common_characters)
# print("sorted list of resultant common alphabets:",common_character_sorted)

#Method2
# String30="sravanthi"
# String40="sravani"
# common=[]
# for char1 in String30:
#     for char2 in String40:
#         if char1==char2:
#             if char1 not in common:
#                 common.append(char1)
# print(common)
# Sorted_order_1=sorted(common)
# print(Sorted_order_1)

#17--->Find the most frequently occurring character in a string
"""
1.create a string
2.create empty dictionary
3.initialize max_value,max_key as zero
4.pick each character using for ,if it is present in dictionary increment the count or else just keep it as 1
5.print the dictionary
6.use for to pick key and value from dictionary 
"""
string21="sravanthi"
occurrence={}
for char in string21:
    if char in occurrence:
        occurrence[char]+=1
    else:
        occurrence[char]=1
print("resultant dictionary is:",occurrence) #result dictionary with key and occurrences
max_value=0
max_key=""
for key,value in occurrence.items():
    if value>max_value:
        max_value=value
        max_key=key
print("maximum key and value is:",max_key,max_value)

#18--->Find the first non-repeating character in a string.
"""
1.Take a string
2.traverse through string using for loop
3.if count of character is exactly one, then it will be a first non repeating character in string,once you found put a break 
4.print that character
"""
string11="sravanthi"
for char1 in string11:
    if string11.count(char1)==1:
        print("first non repeating character is:",char1)
        break

#19--->Reverse a string without using built-in methods.
string21="sravanthi_python"
reverse_string1=""
for char2 in string21:
    reverse_string1=char2+reverse_string1
print("resultant reversed string is:",reverse_string1)


























