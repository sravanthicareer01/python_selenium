name="Sravanthi123@#"
digit=0
characters=0
spl_characters=0
for char in name:
    if char.isalpha():
        characters+=1
    elif char.isdigit():
        digit+=1
    else:
        spl_characters+=1
print("digits are:",digit)
print("characters are",characters)
print("spl_characters are:",spl_characters)
