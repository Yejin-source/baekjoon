# A: 곡의 개수, I: 평균값
A, I = map(int, input().split())

# 최소 멜로디 개수
print(A * (I - 1) + 1)