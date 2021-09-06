import sys
sys.stdin = open('2805.txt', 'r')
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    s = N // 2
    result = 0
    k = 0
    for i in range(s+1):
        if i == (N//2):
            for m in range(N):
                result += arr[i][m]
        else:
            for j in range(s-k, s+k+1):
                result += arr[i][j]
                result += arr[N-i-1][N-j-1]
                k += 1


    print('#{} {}'.format(tc, result))



