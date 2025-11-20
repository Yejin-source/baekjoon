# N: 소들 수, W*H: 헛간 크기, L: 소들 배정 공간
N, W, H, L = map(int, input().split())

# 헛간에 입주 가능한 최대 마리 수
max_cows = (W // L) * (H // L)

print(min(N, max_cows))  # N보다 많을 수 없음