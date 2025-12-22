T = int(input())  # 테스트 케이스 수

for _ in range(T):
    s = int(input())  # 자동차 가격
    n = int(input())  # 옵션 개수

    for _ in range(n):
        # q: 옵션 개수, p: 옵션 가격
        q, p = map(int, input().split())
        s += q * p

    print(s)