#1---> Check whether a number is an Armstrong number
"""
Armstrong number:- sum of cube of digits in number equal to original number
1.Take number as a string
2.convert it into a list
3.we can pick each number and make a cube for it and add each number
4.compare it with original number
5.if it is same its armstrong number or else it's not
"""


# number1="153"
# original_number=int(number1)
# number1_list1=list(number1)
# total=0
# print("list of numbers are:",number1_list1)
# for number1 in number1_list1:
#     cube_number=int(number1)**3
#     print("cube of each number is:",cube_number)
#     total+=cube_number
# print("sum of all numbers is:",total)
# if original_number==total:
#     print(original_number," is an armstrong number")
# else:
#     print(original_number," is not an armstrong number")

#2---> Find the sum of all digits of a number
# number2="154"
# original_number2=int(number2)
# sum2=0
# list_number2=list(number2)
# print("original number is:",original_number2)
# print("list of number2 is:",list_number2)
# for number in list_number2:
#     sum2+=int(number)
# print("sum of digits in number",original_number2,"is:",sum2)

#3---> Check whether user input represents a number
"""
1.we have one function to take input from the terminal,i.e input()
2.once we give the input we can validate the input using predefined fucntions, isdigit(),isalpha() etc
"""
# user_input=input("enter input:")
# if user_input.isdigit():
#     print("given input",user_input,"is number")
# elif len(user_input)==1 and user_input.isalpha():
#     print("given input",user_input,"is alphabet")
# elif user_input.replace(".", "", 1).isdigit():
#     print("Data type: Float")
# else:
#     print(user_input,":is a string")

#4---> Convert decimal numbers to binary, octal and hexadecimal
# user_input=int(input("enter input number"))
# binary=bin(user_input)
# octal=oct(user_input)
# hexa_decimal=hex(user_input)
# print(user_input,":\nbinary",binary,"\noctal",octal,"\nhexadecimal",hexa_decimal)

#5---> Check Fibonacci membership and generate a Fibonacci sequence
# user_input1=int(input("enter input number:"))
# input_check=int(input("enter number to check this number present in series or not"))
# a=0
# b=1
# c=a+b
# fabonacci=[]
# for i in range(user_input1):
#     print(a)
#     fabonacci.append(a)
#     a=b
#     b=c
#     c=a+b
# print("fabonacci sequence is:",fabonacci)
# if input_check in fabonacci:
#     print("present")
# else:
#     print("not present")

#6---> Palindrome program (practise both numeric and string versions)
#String palindrome-radar
# string1="radar"
# string1_list=list(string1)
# #using reversed function
# reversed_string="".join(reversed(string1))
# print("reversed string using reversed function:",reversed_string)
# if string1==reversed_string:
#     print(string1,"is a palindrome")
# else:
#     print(string1,"is not a palindrome")

#using for loop
# using numbers
# number3=input("enter number to check palindrome or not:")
# number3_list=list(number3)
# reversed_number3=""
# for number in number3_list:
#     reversed_number3=number+reversed_number3
# print("reversed number is:",reversed_number3)
# if number3==reversed_number3:
#     print(number3,"is a palindrome")
# else:
#     print(number3,"not a palindrome")
# print("data type of:",type(reversed_number3))
# print("conversion of string to int:",type(int(reversed_number3)))

#7---> Prime number programs
"""
prime number: number divisible by only 1 and itself
if we get reminder is zero when it is divisible by all numbers except 1 and itself then it will be a prime number
so we have to take range from 2 and number, last range will be excluded
"""
# input_number=int(input("enter the number"))
# if input_number<=1:
#     print(input_number,"is not a prime number")
# else:
#     for i in range(2,input_number):
#         if input_number%i==0:
#             print(input_number,"is not a prime number")
#     else:
#             print(input_number,"is a prime number")
#8---> Find the frequency of every digit in a number
input_number1=input("enter the number : ")
input_number_list=list(input_number1)
print("input number list for",input_number1,"is",input_number_list)
dictionary_frequency={}
for element in input_number_list:
    if element in dictionary_frequency:
        dictionary_frequency[element]+=1
    else:
        dictionary_frequency[element]=1
print("frequency of elements in",input_number1,"is:",dictionary_frequency)

#9--->print random numbers
import random
list1 = []
for i in range(5):
    list1.append(random.randint(1, 100))
print("random elements are:",list1)
























