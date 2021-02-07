def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (end + start) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return(binary_search(array, target, start, mid-1))
    else:
        return(binary_search(array, target, mid + 1, end))


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
print(result)
if result == None:
    print(" 찾는 원소가 없습니다. ")
else:
    print("찾는 원소는" + str(result+1) + "번째에 있습니다.")
