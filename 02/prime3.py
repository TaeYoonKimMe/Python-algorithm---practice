prime = [None] * 500
ptr = 0

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5,1001,2):
    i = 0
    while prime[i] * prime[i] <= n:
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1

print(prime)
