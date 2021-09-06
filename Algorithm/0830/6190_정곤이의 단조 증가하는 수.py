import sys
sys.stdin = open('6190.txt', 'r')
for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = -1
    for i in range(N):
        for j in range(i+1, N):
            num = arr[i]*arr[j]

            if result >= num:
                pass
            else:
                a = num % 10    # 첫째자리 수
                b = num
                ans = 0         # 단조 증가하는 수 판별
                while b >= 10:
                    b = b // 10
                    if a >= b % 10:
                        a = b % 10
                        ans = 1
                    else:
                        ans = 0
                        break
                if ans == 1:
                    result = num

    print('#{} {}'.format(tc, result))



