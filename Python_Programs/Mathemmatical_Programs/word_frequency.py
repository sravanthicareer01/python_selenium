#frequency of words
sentence="My name is sravanthi Sravanthi name is"
words=sentence.split()
print("words after splitting is:",words)
result_dict={}
for word in words:
    if word in result_dict:
        result_dict[word]+=1
    else:
        result_dict[word]=1
print("result_dictionary with occurrences are:",result_dict)












