N = int(input())

for i in range(1, N+1):
    spaces = N-i  # 앞쪽 공백

    if i == 1:  # 첫째 줄은 별 하나만
        print(' ' * spaces + '*')

    elif i == N:  # 마지막 줄은 별 가득
        print('*' * (2 * N - 1))

    else:  # 중간 줄은 양쪽 끝에만 별
        inner_spaces = 2 * i - 3
        stars = '*' + ' ' * inner_spaces + '*'
        print(' ' * spaces + stars)