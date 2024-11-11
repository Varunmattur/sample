#count the no of vowels
# count = 0
# word = "education"
# for i in word:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#         count+=1
# print(count)

# or

word=input("Enter the word")
vowel='aeiouAEIOU'
count=0
v=''
for i in word:
    if i in vowel:
        v=v+" "+i
        count+=1
        
print(count)
print(v)

