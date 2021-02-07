n = int(input())

array = []
for _ in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array.sort(key=lambda name: name[1])

for name in array:
    print(name[0], end=' ')
