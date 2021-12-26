def shaker_sort(a):
    left = 0
    right = len(a) - 1
    last = len(a) - 1

    while left < right:
        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i-1]
                last = i
        left = last

        for i in range(left, right):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                last = i
        right = last

