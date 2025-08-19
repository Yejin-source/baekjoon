# 두 개의 자연수
A, B = map(int, input().split())

ax, ay = (A-1) // 4, (A-1) % 4  # A의 좌표 (가로, 세로)
bx, by = (B-1) // 4, (B-1) % 4  # B의 좌표 (가로, 세로)

# 두 좌표 간 거리 출력
print(abs(ax-bx) + abs(ay-by))  # abs(): 절댓값