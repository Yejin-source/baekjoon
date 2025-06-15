# 색종이의 수
N = int(input())

# 도화지 범위 초기화
paper = [[0] * 100 for _ in range(100)]  # 리스트 컴프리헨션


# N번 반복
for _ in range(N):
    x, y = map(int, input().split())

    # 가로 10칸, 세로 10칸 색종이 영역을 1로 표시
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1  # 색종이가 붙은 칸은 1로 표시

# 색종이가 붙은 영역의 넓이 계산
result = 0
for k in paper:
    result += k.count(1)  # 각 줄의 1 개수 더하기

print(result)


# 리스트 컴프리헨션
# 파이썬에서 리스트를 간결하게 만들 수 있는 문법

# 100x100 크기의 2차원 리스트를 만드는 for문
# paper = []
# for _ in range(100):
#     row = [0] * 100
#     paper.append(row)

# 리스트 컴프리헨션을 사용한 경우
# paper = [[0] * 100 for _ in range(100)]