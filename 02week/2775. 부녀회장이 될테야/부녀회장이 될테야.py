
# 0.5초 -> 1000만회
# 아파트 전체를 구성

# 브루트포스로 구성해도 문제없을 듯 해서 해봄
bu = [[] * 15 for _ in range(15)]
# 최초 층 채우기
for i in range(14):
    bu[0].append(i + 1)
# 이후 층 채우기
# 이 부분이 2중 for문 + sum 연산으로 n^3의 복잡도
for i in range(1, 15):  # 층
    for j in range(1, 15):  # 호
        bu[i].append(sum(bu[i - 1][:j]))

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    print(bu[k][n - 1])

# # 브루트포스2 개선
# bu = [[0] * 15 for _ in range(15)]
# # 최초 층 채우기
# for i in range(14):
#     bu[0][i] = i + 1
# # 이후 층 채우기
# # 이 부분이 2중 for문에 sum연산을 제거한 n^2 복잡도
# for i in range(1, 15):  # 층
#     for j in range(14):  # 호
#         # 매 층 1호는 무조건 1
#         if j == 0:
#             bu[i][j] = 1
#         # 직전 호실 + 아랫층 같은 호실 = 현재 호실
#         else:
#             bu[i][j] = bu[i][j-1] + bu[i-1][j]
#
# for _ in range(int(input())):
#     k = int(input())
#     n = int(input())
#
#     print(bu[k][n - 1])
