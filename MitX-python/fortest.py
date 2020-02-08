n=0
for n in range(5):
    print(n)

mysum=0
for n in range(7, 10):
    mysum += n

print(mysum)

mytest=0

for n in range(5,11,2):
    mytest += n
    if(n==7):
        break

print(mytest)
