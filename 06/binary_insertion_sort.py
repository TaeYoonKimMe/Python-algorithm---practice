def binary_insertion_sort(a):

    n = len(a)
    for i in range(1, n):
        pl = 0
        pr = i - 1
        temp = a[i]

        while pl <= pr:
            pc = (pl + pr) // 2
            if a[pc] == temp:
                break
            elif a[pc] < temp:
                pl = pc + 1
            else:
                pr = pc - 1

        pd = pc + 1 if pl <= pr else pr + 1
        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = temp

if __name__ == '__main__':
    print('이진 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    binary_insertion_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')