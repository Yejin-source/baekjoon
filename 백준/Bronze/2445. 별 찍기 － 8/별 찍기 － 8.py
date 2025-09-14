N = int(input())

# 위쪽
for i in range(1, N+1):
    stars = '*' * i
    spaces = ' ' * (N - i) * 2
    print(stars + spaces + stars)

# 아래쪽
for i in range(N-1, 0, -1):
    stars = '*' * i
    spaces = ' ' * (N - i) * 2
    print(stars + spaces + stars)