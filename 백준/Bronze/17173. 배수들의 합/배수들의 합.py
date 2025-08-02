# N: 범위, M: 기준 수 개수
N, M = map(int, input().split())

# 기준 수 리스트
K = list(map(int, input().split()))

total = 0

for num in range(1, N+1):
    for factor in K:
        if num % factor == 0:
            total += num  # 배수라면 값을 누적
            break         # 한 번만 더하고 다음 숫자로 이동

print(total)