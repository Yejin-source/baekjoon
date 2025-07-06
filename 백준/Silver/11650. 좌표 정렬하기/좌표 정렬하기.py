# 점의 개수
N = int(input())

points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))  # (x, y) 좌표를 튜플로 저장

# (x, y) 순으로 오름차순 정렬
points.sort()

for x, y in points:
    print(x, y)