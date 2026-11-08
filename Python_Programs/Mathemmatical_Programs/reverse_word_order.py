# sentence="My name is sravanthi"
# words=sentence.split()
# print("words after split",words)
# first_word=print("first word is",words[0])
# words[3],words[0] = words[0],words[3]
# print("resultant list after swapping positions of 0 and 3 is:",words)

# sentence1="My name is sravanthi1"
# words=sentence.split()
# print("words after splitting sentence:",words)
# reversed_list=words[::-1]
# print(reversed_list)

sentence2="My name is sravanthi2"
words2=sentence2.split()
print("words after splitting are:",words2)
print("reversed_order is:",words2[::-1])
result_list2=""
for word in words2:
    reverse2=""
    for char in word:
        reverse2=char+reverse2
    print(reverse2)
    result_list2=result_list2+reverse2+" "
print(result_list2)















