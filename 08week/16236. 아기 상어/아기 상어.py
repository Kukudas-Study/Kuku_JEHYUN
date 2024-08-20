from collections import deque

# 범위 체크
def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

# 먹을 물고기를 탐색하는 함수
def find_feed(shark):
    # bfs로 넓이 탐색
    visited = [[False] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = True
    q = deque([[shark[0], shark[1], 0]])  # y, x, 거리
    candidates = []  # 먹을 수 있는 물고기들 (y, x, 거리)

    while q:
        y, x, dist = q.popleft()

        for dy, dx in d:
            ny, nx = y + dy, x + dx
            # 범위 밖이 아니고, 아기상어보다 크지 않다면
            if in_range(ny, nx) and not visited[ny][nx]:
                if ground[ny][nx] <= shark_size[0]:  # 지나갈 수 있는 칸
                    visited[ny][nx] = True
                    if ground[ny][nx] < shark_size[0] and ground[ny][nx] != 0:  # 먹을 수 있는 물고기
                        candidates.append([ny, nx, dist + 1])
                    q.append([ny, nx, dist + 1])

    # 물고기를 정렬: 거리 -> y 좌표 -> x 좌표 순으로 정렬
    if candidates:
        candidates.sort(key=lambda x: (x[2], x[0], x[1]))
        return candidates[0]  # 가장 가까운 물고기 반환
    return [-1, -1, 0]

# 아기상어의 위치를 찾는 함수(최초 1회만 실행)
def find_baby():
    for i in range(n):
        for j in range(n):
            if ground[i][j] == 9:
                return [i, j, 0]

n = int(input())
ground = [list(map(int, input().split())) for _ in range(n)]
# 4방향 (가장 위, 가장 왼쪽 순이니 반시계방향 탐색)
d = [[-1, 0], [0, -1], [1, 0], [0, 1]]

# 상어 위치 미리 찾기 | 초기 상어 크기 2
baby_shark = find_baby()
ground[baby_shark[0]][baby_shark[1]] = 0  # 상어 위치 초기화
shark_size = [2, 0]  # 크기, 먹은 물고기 수
time = 0

while True:
    fish_position = find_feed(baby_shark)
    if fish_position[0] == -1:  # 먹을 물고기가 없다면 종료
        break

    # 상어를 물고기 위치로 이동시키고, 먹은 물고기 처리
    baby_shark[0], baby_shark[1] = fish_position[0], fish_position[1]
    ground[baby_shark[0]][baby_shark[1]] = 0  # 먹은 물고기 위치를 빈칸으로 만듦
    shark_size[1] += 1  # 물고기 하나 먹음

    # 상어가 자신의 크기만큼 물고기를 먹으면 크기가 증가
    if shark_size[0] == shark_size[1]:
        shark_size[0] += 1
        shark_size[1] = 0

    time += fish_position[2]  # 이동한 시간 추가

print(time)
