n, m = map(int, input().split())

w = list(map(int, input().split()))
result = 0
w.sort()
for i in range(len(w)-1):
    if w[i] != w[i+1]:
        result += (n-(i+1))*
