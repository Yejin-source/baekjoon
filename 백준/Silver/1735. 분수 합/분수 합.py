from math import gcd

# 첫 번째 분수 A/B
A, B = map(int, input().split())

# 두 번째 분수 C/D
C, D = map(int, input().split())

# 두 분수의 합: A/B + C/D = (A×D + C×B) / (B×D)
num = A * D + C * B  # 분자
den = B * D          # 분모

# 최대공약수 계산
gcd_val = gcd(num, den)

# 최대공약수로 나눠 기약분수 출력
print(num // gcd_val, den // gcd_val)