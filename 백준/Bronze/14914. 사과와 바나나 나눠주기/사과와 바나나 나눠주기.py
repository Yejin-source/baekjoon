# a: 사과 개수, b: 바나나 개수
a, b = map(int, input().split())

# 나누어 줄 수 있는 모든 경우 계산
for x in range(1, min(a, b) + 1):
    if a % x == 0 and b % x == 0:
        # x명에게 사과 a/x개, 바나나 b/x개 배분
        print(x, a // x, b // x)