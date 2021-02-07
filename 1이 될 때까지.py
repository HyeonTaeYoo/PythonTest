n,k = map(int, input().split())
cnt=0
while n!=1 :
    if n%k==0:
        n=n//k
    else:
        n= n-1
    cnt+=1
    
print(cnt)

if n<k:
    print("Error! N must be bigger than K")