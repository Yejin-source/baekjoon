T = int(input())  # 테스트 케이스 수

prices = [350.34, 230.90, 190.55, 125.30, 180.90]

for _ in range(T):
    count = list(map(int, input().split()))

    total = 0
    
    for c, p in zip(count, prices):
        total += c * p

    # 소수점 둘째 자리까지 출력
    print(f"${total:.2f}")