#first 10 fibbonacci series
f0=0
f1=1
print(f0,end=" ")
print(f1,end=" ")
for i in range(1,9):
    f2=f0+f1
    print(f2,end=" ")
    f0=f1
    f1=f2
    