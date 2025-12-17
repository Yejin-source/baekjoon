# N: 환전한 금액, M: 묶음 크기
N, M = map(int, input().split())

total = 0  # 전체 센 횟수

while N > 0:
    total += N  # 현재 센 횟수
    N //= M     # 묶음 변환

print(total)