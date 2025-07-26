N = int(input())

for i in range(N, 0, -1):  # N부터 1까지 감소
    space = ' ' * (N - i)
    stars = '*' * i
    print(space + stars)