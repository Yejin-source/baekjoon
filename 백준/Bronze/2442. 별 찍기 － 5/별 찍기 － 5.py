N = int(input())

for i in range(1, N+1):
    spaces = ' ' * (N - i)   # 앞쪽 공백
    stars = '*' * (2*i - 1)
    print(spaces + stars)