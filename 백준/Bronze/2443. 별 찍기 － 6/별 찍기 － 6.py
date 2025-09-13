N = int(input())

# N행부터 1행까지 거꾸로 내려오면서 출력
for i in range(N, 0, -1):
    spaces = ' ' * (N - i)  # 앞쪽 공백
    stars = '*' * (2*i - 1)
    print(spaces + stars)