T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    # N: 우주선 개수, D: 목적지까지 거리
    N, D = map(int, input().split())

    count = 0

    for _ in range(N):
        # v: 우주선 최고속도, f: 연료양, c: 연료소비율
        v, f, c = map(int, input().split())

        if v * f >= D * c:
            count += 1

    print(count)