T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    # N: 소유한 쿠키 개수, C: 매일 먹는 쿠키 개수
    N, C = map(int, input().split())

    print((N+C-1) // C)  # 쿠키를 먹을 수 있는 총 일수