N = int(input())

for i in range(1, N+1):
    spaces = N-i  # 앞쪽 공백

    if i == 1:  # 첫째 줄은 별 하나만
        print(' ' * spaces + '*')

    else:  # 둘째 줄부터는 양쪽 끝에만
        inner_spaces = 2 * i - 3  # 가운데 공백
        stars = '*' + ' ' * inner_spaces + '*'
        print(' ' * spaces + stars)