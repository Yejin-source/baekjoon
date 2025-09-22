N = int(input())

# 위쪽 (가운데 포함)
for i in range(1, N+1):
    print(' ' * (N-i) + '*' * i)

# 아래쪽 (가운데 제외)
for i in range(N-1, 0, -1):
    print(' ' * (N-i) + '*' * i)