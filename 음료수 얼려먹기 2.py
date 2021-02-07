from collections import deque

n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input())))


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = deque.popleft()
        print(v, end='')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
