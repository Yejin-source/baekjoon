import math

# 두 정수
A, B = map(int, input().split())

# 최소공배수(LCM) = A * B // 최대공약수(GCD)
print(A * B // math.gcd(A, B))