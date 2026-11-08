name="sravanthi"
vowels="aeiouAEIOU"
#convert string into list
result_vowels=list(vowels)
vowels_found=[]
print(result_vowels)
count = 0
for char in name:

    if char in result_vowels:
        count+=1
        vowels_found+=char
print("vowel count is",count)
print("vowels are",vowels_found)



