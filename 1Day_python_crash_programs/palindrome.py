string1="sravanthi"
string2="maam"
print("strings are",string1,string2)
rev_string1=string1[::-1]
rev_string2=string2[::-1]
print("reversed strings are:",rev_string1,rev_string2)
if string2==rev_string2:
    print(string2,"is palindrome")
else:
    print("its not a palindrome")
