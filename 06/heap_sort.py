def heap_sort(a):

    def down_heap(a, left, right):

        tmp = a[left]

        parent = left

        while parent < (right + 1) // 2:
            cl = 2 * parent + 1
            cr = cl + 1

            cd = cr if cr <= right and a[cr] > a[cl] else cl

            if tmp >= a[cd]:
                break
            a[parent] = a[cd]
            parent = cd
        a[parent] = tmp

    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        down_heap(a, i, n-1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i - 1)


if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
