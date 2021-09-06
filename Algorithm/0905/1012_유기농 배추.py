import sys
sys.stdin = open('1012.txt', 'r')
def dfs(x, y):
    # 인접한 위치 탐색
    r = [0, 0, -1, 1]
    c = [1, -1, 0, 0]
    for i in range(4):
        rx = x + r[i]
        cy = y + c[i]
        # 범위내에 있고 배추가 있으면 (1) 0으로 만들어준다.
        if 0 <= rx < N and 0 <= cy < M and cabbage[rx][cy] == 1:
            cabbage[rx][cy] = 0
            # 인접 배추들을 다 0으로 만들기 위해 dfs함수를 또 호출한다.
            dfs(rx, cy)

for tc in range(1, int(input())+1):
    # M = 배추밭 가로  N = 배추밭 세로  K = 배추가 심어져있는 위치의 개수
    M, N, K = map(int, input().split())
    cabbage = [[0]*M for _ in range(N)]
    cnt = 0
    # 배추 위치를 1로 바꾸기
    for _ in range(K):
        a, b = map(int, input().split())
        cabbage[b][a] = 1
    # cabbage를 탐색했을 때 1이면 cnt += 1 하고 인접한 곳 0으로 바꾸기
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)


