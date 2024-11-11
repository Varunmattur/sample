#no is a prime or not
prime=True
n = int(input())
for i in range(2,n):
    if(n%i==0):
        prime=False
        break
if prime==False:
    print(f"{n} is not a prime no.")    
else:
    print(f"{n} is a prime no.")