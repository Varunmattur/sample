#frequency of each character
word = "programming"
frequency={}

for char in word:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
    
for char,count in frequency.items():
    print(f"'{char}' : {count}")