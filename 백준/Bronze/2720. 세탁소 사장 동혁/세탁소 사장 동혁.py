# 테스트 케이스 수
T = int(input())

# T번 반복
for _ in range(T):
    # 거스름돈 (센트)
    C = int(input())

    # 큰 단위 동전부터 순서대로 확인
    for i in [25, 10, 5, 1]:
        # 각 동전 개수 출력
        print(C // i, end=' ')
        # 남은 금액 계산
        C = C % i
    print()  # 줄바꿈