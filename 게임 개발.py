n, m = map(int, (input().split()))

x, y, direct = map(int, input().split())

map_info = []

for i in range(n):
    map_info.append(list(map(int, input().split())))

#print(map_info)
d = [[0]*m for _ in range(n)]
d[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1


def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3


turn_time = 0

while True:

    turn_left()
    nx = x + dx[direct]
    ny = y + dy[direct]

    if map_info[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    if turn_time == 4:
        nx = x-dx[direct]
        ny = y-dy[direct]

        if map_info[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break
        turn_time = 0


print(cnt)
