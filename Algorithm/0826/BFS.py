import sys
sys.stdin = open('5105.txt', 'r')
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 시작점, 도착점
    # maze -> 그래프 처럼 사용
    # visit => 방문표시 및 거리를 저장
    # Queue
    visit = [[0]*N for _ in range(N)]
    sr = sc = er = ec = 0
    for i in range(N):    # 시작/도착 위치 찾기
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j
            elif maze[i][j] == 3:
                er, ec = i, j
    # 큐를 생성하고, 시작점을 삽입, 시작점 방문표시
    Q = [[sr, sc]]
    visit[sr][sc] = 1
    # 빈큐가 아닐동안 반복
    while Q:
        # 큐에서 정점([r, c])을 하나 꺼내온다.
        # 방문하지 않은 인접정점을 찾는다
        # [r, c]의 상하좌우 좌표를 생성([nr, nc])해서 확인한다.
        # !!!!!중요 ==> 좌표 생성후에는 반드시 인덱스 범위 체크
        # maze[nr][nc]를 삽입하고, visit[nr][nc] = visit[n][r] + 1
        r, c = Q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            if maze[nr][nc] == 1 or visit[nr][nc] != 0: continue

            visit[nr][nc] = visit[r][c] + 1
            Q.append([nr, nc])
    # 도착점까지 경로가 없다면 visit[er][ec] == 0
    if visit[er][ec]:
        visit[er][ec] -= 2
    print(visit[er][ec])


