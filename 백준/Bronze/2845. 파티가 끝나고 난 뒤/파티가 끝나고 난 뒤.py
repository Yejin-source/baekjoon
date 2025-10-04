# L: 1m^2당 사람 수, P: 파티 장소 넓이
L, P = map(int, input().split())

# 각 기사에 실려있는 참가자 수
nums = list(map(int, input().split()))

total = L * P  # 실제 참가자의 수

for n in nums:
    print(n - total, end=' ')