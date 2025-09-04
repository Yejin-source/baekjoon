# 컵의 위치를 바꾼 횟수
M = int(input())

ball = 1  # 공은 처음에 1번 컵 아래

for _ in range(M):
    # 서로 위치를 바꿀 두 컵 번호
    X, Y = map(int, input().split())
    
    if ball == X:
        ball = Y
    elif ball == Y:
        ball = X

print(ball)