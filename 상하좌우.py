
n = int(input())
Direct = list(input().split())
x,y =1,1

for i in range(len(Direct)):
    if Direct[0] == 'R':
        if x==n:
            pass
        else:
            x+=1
        Direct.pop(0)

    elif Direct[0] == 'L':
        if x!=1:
            x-=1
        Direct.pop(0)

    elif Direct[0] == 'U':
        if y==1:
            pass
        else:
            y-=1
        Direct.pop(0)

    elif Direct[0] == 'D':
        if y==n:
            pass
        else:
                y+=1
        Direct.pop(0)
print(y,x)
