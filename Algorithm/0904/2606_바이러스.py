import sys
sys.stdin = open('2606.txt', 'r')
#인접행렬 방식을 이용해 DFS를 구현
# DFS 함수
def dfs(s):
    global cnt
    visit[s] = 1
    for e in range(1, N+1):
        if graph[s][e] == 1 and visit[e] == 0:
            cnt += 1
            dfs(e)
    return cnt

N = int(input())  # 컴퓨터의 수
M = int(input())  # 간선의 개수
cnt = 0    # 탐색 결과개수

# 경로 저장
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visit = [0]*(N+1)  # 방문 처리

print(dfs(1))



