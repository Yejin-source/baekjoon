# N × M 초콜릿 -> 쪼갤 때마다 +1 조각
# 최소 쪼개기 횟수 = N * M - 1

N, M = map(int, input().split())
print(N * M - 1)