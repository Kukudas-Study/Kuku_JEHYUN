# 8방향 이동을 위한 방향 벡터 정의
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def move(balls):
    # 모든 파이어볼을 이동시키고, 각 칸에 있는 파이어볼의 개수를 기록합니다.
    next_balls = []
    for ball in balls:
        y, x, m, s, d = ball
        # 새로운 위치 계산 (모듈로 연산으로 격자판의 경계를 넘지 않도록 함)
        y, x = (y + s * dy[d]) % N, (x + s * dx[d]) % N
        visited[y][x] += 1  # 새로운 위치에 파이어볼이 있음을 기록
        next_balls.append([y, x, m, s, d])  # 이동 후의 파이어볼 상태 저장

    return next_balls


def four_move(balls):
    # 같은 칸에 있는 파이어볼을 합쳐서 새로운 파이어볼을 생성합니다.
    next_balls = []
    for ball in balls:
        y, x, m, s, di = ball
        if visited[y][x] == 1:
            # 현재 위치에 파이어볼이 하나만 있으면 그대로 유지
            next_balls.append([y, x, m, s, di])
        elif visited[y][x] >= 2:
            # 같은 위치에 여러 개의 파이어볼이 있으면 합쳐서 새로운 파이어볼 생성
            if not Map[y][x]:
                Map[y][x] = [m, s, [di]]
            else:
                Map[y][x][0] += m
                Map[y][x][1] += s
                Map[y][x][2].append(di)

    # 합쳐진 위치에 대해 새로운 파이어볼 생성
    for y in range(N):
        for x in range(N):
            if Map[y][x]:
                m, s, d = Map[y][x]
                # 질량이 0이면 소멸되므로, 새로운 파이어볼 생성 (질량, 속도, 방향 설정)
                _m, s = m // 5, s // visited[y][x]
                d = direction(d)  # 방향 결정
                for dir in d:
                    next_balls.append([y, x, _m, s, dir])

    return next_balls


def direction(dirs):
    # 파이어볼의 방향을 결정합니다. 모든 방향이 홀수거나 모두 짝수일 경우 각각 0, 2, 4, 6 또는 1, 3, 5, 7
    cnt = 0
    for d in dirs:
        if not (d % 2):
            cnt += 1
    if not cnt or cnt == len(dirs):
        return [0, 2, 4, 6]
    return [1, 3, 5, 7]


def delete(balls):
    # 질량이 0인 파이어볼을 제거합니다.
    next_balls = []
    for i in range(len(balls)):
        if balls[i][2] > 0:  # 질량이 0보다 큰 파이어볼만 유지
            next_balls.append(balls[i])
    return next_balls


# 입력
N, M, K = map(int, input().split())  # 격자 크기 N, 파이어볼 개수 M, 명령 횟수 K
balls = [list(map(int, input().split())) for _ in range(M)]  # 각 파이어볼의 정보
ans = 0

# 파이어볼의 위치를 0-index로 조정
for ball in balls:
    ball[0] -= 1
    ball[1] -= 1

# K번의 명령을 반복
for _ in range(K):
    Map = [[0] * N for _ in range(N)]  # 각 위치에 있는 파이어볼의 질량과 속도 합을 저장할 맵
    visited = [[0] * N for _ in range(N)]  # 각 위치에 파이어볼 개수를 기록할 배열
    balls = move(balls)  # 모든 파이어볼 이동
    balls = four_move(balls)  # 이동 후 합쳐지는 과정
    balls = delete(balls)  # 질량이 0인 파이어볼 제거

# 남아 있는 파이어볼의 질량 총합 계산
for ball in balls:
    ans += ball[2]

print(ans)
