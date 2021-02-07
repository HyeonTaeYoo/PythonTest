s = list(input())
print(len(s))

cnt0 = 0
cnt1 = 0

if s[0] == '0':
    cnt1 += 1
else:
    cnt0 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            cnt1 += 1
        else:
            cnt0 += 1


min_cnt = min(cnt0, cnt1)

print(min_cnt)

for i in range(len(s)):
    print(i)
