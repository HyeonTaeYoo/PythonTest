import sys


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return (binary_search(array, target, start, mid-1))
    else:
        return (binary_search(array, target, mid+1, end))


if __name__ == "__main__":
    n = int(input())
    array1 = list(map(int, sys.stdin.readline().rstrip().split()))
    array1.sort()
    m = int(input())
    array2 = list(map(int, sys.stdin.readline().rstrip().split()))

    # for i in array2:
    #     if binary_search(array1, i, 0, n-1) != None:
    #         print(str(i)+"는 존재합니다 : Yes")
    #     else:
    #         print(str(i)+"는 존재하지 않습니다 : No")
    for i in array2:
        if i in array1:
            print(str(i)+"는 존재합니다 : Yes")
        else:
            print(str(i)+"는 존재하지 않습니다 : No")
