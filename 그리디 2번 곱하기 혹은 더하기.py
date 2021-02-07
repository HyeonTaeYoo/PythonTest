n = list(map(int, input()))

length = len(n)
result = 1
for i in range(length):
    if n[i] != 0:
        result *= n[i]
    else:
        result += n[i]

print(result)
