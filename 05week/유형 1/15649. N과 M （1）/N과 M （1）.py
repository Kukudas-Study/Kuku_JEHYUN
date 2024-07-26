# ===================================간단한 풀이==================
# 사실 이문제는 이렇게 해도 아무런 문제가 없는 문제...
# N, M = map(int, input().split())
# lst = []
# def dfs(start):
#     if len(lst) == M:
#         print(*lst)
#         return
#     else:
#         for i in range(1, N+1):
#             if i not in lst:
#                 lst.append(i)
#                 dfs(i)
#                 lst.pop()
# dfs(1)
# ================================================================

def back(cnt):
    # 출력 시점
    if cnt == m:
        for i in ans:
            print(i, end=" ")
        print()
        return
    # 하나씩 순회하면서 백트래킹 넣기
    for i in range(1, n+1):
        # 방문했으면 다음거
        if visit[i]: continue
        # 메인의 for문 안 동작과 동일
        visit[i] = True
        ans.append(i)
        # 자리수 맞추기
        back(cnt+1)
        ans.pop()
        visit[i] = False

n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
ans = []
visit = [False for _ in range(n+1)]
# 백트래킹 시작점
for i in range(1, n+1):
    # 방문 찍고
    visit[i] = True
    # 출력할 list에 넣고
    ans.append(i)
    # 백트래킹으로 차곡차곡 쌓기
    back(1)
    # 함수가 끝나면 list 비우고, 방문 지우기
    ans.pop()
    visit[i] = False
