n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

# array.sort()
# array.reverse()

array = sorted(array, reverse=True)

# for i in range(len(array)):
#     print(array[i], end=" ")

for i in array:
    print(i, end=' ')
