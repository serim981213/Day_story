import sys
sys.stdin = open('1220.txt')
for tc in range(1, 11):
    # 각 행, 열의 개수
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 교착상태 count
    cnt = 0
    for i in range(N):
        for j in range(N):
            # arr[i][j] == 1인 경우 i 이후의 열을 돌면서 2를 찾는다.
            if arr[i][j] == 1:
                for m in range(i+1, N):
                    # 1이 찾아질 경우 이후에 cnout될 수 있으므로 2를 찾는 for문을 나간다.
                    if arr[m][j] == 1:
                        break
                    elif arr[m][j] == 2:
                        cnt += 1
                        break
    print('#{} {}'.format(tc, cnt))