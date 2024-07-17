from collections import deque

def dfs(start):
    # 방명록 찍기
    visited[start] = True
    rlt.append(start)
    # 해당 노드에서 갈 수 있는 위치로 이동
    for node in nodes[start]:
        # 방문한적 있다면 패스
        if visited[node]:
            continue
        # 재귀
        dfs(node)

def bfs(start):
    # 첫 노드 방문 체크
    visited[start] = True
    # 노드 담을 리스트
    q = deque([])
    # 시작을 담고
    q.append(start)
    # 더이상 갈 곳이 없을 때 까지
    while q:
        # 하나씩 뽑아서 탐색
        s = q.popleft()
        # 순서대로 담기
        rlt.append(s)
        for node in nodes[s]:
            # 방문했다면 패스
            if visited[node]:
                continue
            q.append(node)
            # 방문 체크
            visited[node] = True


n, m, v = map(int, input().split())
nodes = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
    
# 오름차순 배열
for i in range(1, n+1):
    nodes[i].sort()

visited = [False] * (n+1)
rlt = []
dfs(v)
print(*rlt)
visited = [False] * (n+1)
rlt = []
bfs(v)
print(*rlt)
