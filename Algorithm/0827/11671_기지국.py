import sys
sys.stdin = open('11671.txt', 'r')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스 체크, H일때 X로 바꾸기
        for j in range(ord(arr[x][y])-ord('A')+1):
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                arr[nx][ny] = 'X'
                nx = nx + dx[i]
                ny = ny + dy[i]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 0
    # 기지국 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
                check(i, j)

    # 4방향 돌려서 커버되는 H -> X
    # H 세기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                ans += 1
    print('#{} {}'.format(tc, ans))

