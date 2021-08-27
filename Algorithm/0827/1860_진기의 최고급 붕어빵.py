import sys
sys.stdin = open('1860.txt')
for tc in range(1, int(input())+1):
    # N:예약손님 수, M초의 시간을 들이면 K개의 붕어빵 만들 수 있다.
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 'Possible'
    # 손님이 들어오는 순서를 정렬하자
    arr.sort()

    for i in range(N):
        tmp = (arr[i] // M) * K
        if tmp - 1 -i < 0:  # -1은 현재 손님꺼, i는 이전 손님들이 가져간 수
            ans = 'Impossible'
            break

    print('#{} {}'.format(tc, ans))



