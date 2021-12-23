prime = [None] * 500
ptr = 0

prime[ptr] = 2
ptr += 1

for n in range(3,1001,2):
    for i in range(0,ptr):
        if n%prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1

print(prime)