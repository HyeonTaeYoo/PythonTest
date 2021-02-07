n = int(input())
scare = list(map(int, input().split()))

scare.sort()
print(scare)
cnt = 0

while True:
    m = int(scare.pop())
    for _ in range(m-1):
        scare.pop()
    cnt += 1
    if not len(scare):
        break

print(cnt)
