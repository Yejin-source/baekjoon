# 시, 분, 초
A, B, C = map(int, input().split())

D = int(input())  # 조리 시간 (초)                   

# 초로 변환 후 더하기
total = A * 3600 + B * 60 + C + D

h = (total // 3600) % 24  # 시
m = (total % 3600) // 60  # 분
s = total % 60            # 초

print(h, m, s)