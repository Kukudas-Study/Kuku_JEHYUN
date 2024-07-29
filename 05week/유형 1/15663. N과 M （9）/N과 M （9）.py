def back():
    # 길이 맞고 해당 리스트가 결과에 없다면 append
    if len(ans) == m:
        # 튜플은 불변이라 여기서 바꿔주기
        ans_tuple = tuple(ans)
        rlt.add(ans_tuple)
        return
    for i in range(n):
        # 방문 찍 턴
        if visit[i]: continue
        visit[i] = True
        ans.append(lst[i])
        back()
        visit[i] = False
        ans.pop()

n, m = map(int, input().split())
# 동시에 오름차순
lst = sorted(list(map(int, input().split())))
ans = []
rlt = set()
visit = [False] * n
back()
# set을 다시 리스트로
rlt_list = sorted(list(rlt))
for r in rlt_list:
    print(*r)