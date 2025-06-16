# 점의 개수
N = int(input())

xs = []  # x좌표 저장리스트
ys = []  # y좌표 저장리스트


# N번 반복
for _ in range(N):
    x, y = map(int, input().split())  # 각 점의 x, y 좌표
    xs.append(x)
    ys.append(y)


# 가로 길이 = x좌표 최댓값 - 최솟값
width = max(xs) - min(xs)

# 세로 길이 = y좌표 최댓값 - 최솟값
height = max(ys) - min(ys)

# 최소 크기의 직사각형 넓이 출력
print(width * height)