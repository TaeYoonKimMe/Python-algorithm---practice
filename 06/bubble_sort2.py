def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        count = 0
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                count += 1
        if count == 0:
            break