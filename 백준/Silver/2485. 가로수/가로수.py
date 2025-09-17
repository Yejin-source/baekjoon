import math

N = int(input())  # 이미 심어져 있는 가로수의 수
trees = [int(input()) for _ in range(N)]  # 각 가로수의 위치

# 각 가로수 간격 리스트
distances = [trees[i+1] - trees[i] for i in range(len(trees)-1)]


# 모든 간격의 최대공약수
gcd = distances[0]
for d in distances[1:]:
    gcd = math.gcd(gcd, d)

# 각 구간마다 (현재 간격/최대공약수 간격 - 1)
need = sum(d//gcd - 1 for d in distances)

# 새로 심어야 하는 가로수의 최소 수 출력
print(need)