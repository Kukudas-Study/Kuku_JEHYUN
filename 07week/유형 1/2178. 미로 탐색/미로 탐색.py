from collections import deque

def in_range(y, x):
    return 0<=y<n and 0<=x<m

def bfs():
    d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visit = set()
    y, x = 0, 0
    visit.add((y, x))
    # 각 depth 마다 기록해주려고 cnt를 0 으로
    q = deque([(y, x, 1)])
    while(q):
        sy, sx, cnt = q.popleft()
        if (sy, sx) == (n-1, m-1):
            return cnt
        for dy, dx in d:
            ny, nx = sy+dy, sx+dx
            if in_range(ny, nx) and (ny, nx) not in visit and maze[ny][nx]:
                visit.add((ny, nx))
                q.append((ny, nx, cnt+1))


n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

# 1 -> 길 / 0 -> 벽 / (0, 0) -> (n-1, m-1) 위치로

print(bfs())
