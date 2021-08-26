import sys
sys.stdin = open('3499.txt', 'r')
for tc in range(1, int(input())+1):
    N = int(input())
    cards = input().split()
    # 결과를 출력한 result 리스트
    result = ['']*N
    # N이 짝수일 경우
    if N % 2 == 0:
        for i in range(N):
            # N//2보다 작은 인덱스의 카드는 자기 인덱스의 2배인 짝수번째에 들어간다
            if i < N//2:
                result[2*i] = cards[i]
            # N//2 보다 큰 인덱스는 계산을 쉽게하기위해 N//2를 빼주고 *2 +1 해주어 홀수번째에 들어간다
            else:
                result[(i-N//2)*2 +1] = cards[i]
    else:
        for i in range(N):
            if i < N//2 + 1:
                result[2*i] = cards[i]
            else:
                result[(i-N//2-1)*2 + 1] = cards[i]
    print('#{} '.format(tc), end='')
    for k in range(N):
        print(result[k], end=' ')
    print()

