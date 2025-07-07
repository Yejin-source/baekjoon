# 점의 개수
N = int(input())

points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((y, x))  # (y, x) 순으로 저장

# (y, x) 순으로 오름차순 정렬
points.sort()

for y, x in points:
    print(x, y)  # (x, y) 로 출력