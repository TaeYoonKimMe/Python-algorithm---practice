def med(a, idx1, idx2, idx3):
    if a[idx1] > a[idx2]:
        a[idx1], a[idx2] = a[idx2], a[idx1]
    if a[idx2] > a[idx3]:
        a[idx2], a[idx3] = a[idx3], a[idx2]
    if a[idx1] > a[idx2]:
        a[idx1], a[idx2] = a[idx2], a[idx1]
    return idx2


def insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        j = i
        tmp = a[i]

        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp


def qsort(a, left, right):

    if right - left + 1 < 9:
        insertion_sort(a)

    else:
        pl = left
        pr = right
        pc = (pl + pr) // 2
        m = med(a, pl, pc, pr)
        x = a[m]

        a[m], a[pr-1] = a[pr-1], a[m]

        pl += 1
        pr -= 2

        while pl <= pr:
            while a[pl] < x:
                pl += 1
            while a[pr] > x:
                pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr:
            qsort(a, left, pr)
        if pl < right:
            qsort(a, pl, right)


def quick_sort(a):
    qsort(a, 0, len(a) - 1)


if __name__ == '__main__':
    print('퀵 정렬을 합니다(원소 수가 9 미만이면 단순 삽입 정렬을 합니다,')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
