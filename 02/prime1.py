x = []

for i in range(2,1001):

    for n in range(2,i):
        if(i%n==0): break
    else:
        x.append(i)

print(x)