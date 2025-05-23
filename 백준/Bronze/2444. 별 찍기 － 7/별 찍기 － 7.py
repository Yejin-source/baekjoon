N = int(input())

# 위쪽 삼각형 (1부터 N줄까지)
for i in range(1, N+1):
    blank = ' ' * (N - i)
    star = '*' * (2 * i - 1)  # 1, 3, 5, ...
    print(blank + star)

# 아래쪽 삼각형 (N-1부터 1줄까지)
for i in range(N-1, 0, -1):
    blank = ' ' * (N - i)
    star = '*' * (2 * i - 1)  # 감소하는 별 개수 (2N-3, 2N-5, ..., 1)
    print(blank + star)


# 처음에 접근한 방식 (홀수/짝수 구분)
# N = int(input())

# 위쪽 삼각형 (홀수)
# for i in range(2*N-1):
#     if i % 2 != 0:
#         star = '*' * i
#         blank = ' ' * ((2*N-1-i) // 2)
#         print(blank + star)
    
# 아래쪽 삼각형 (짝수)
# for i in range(2*N-1):
#     if i % 2 == 0:
#         star = '*' * (2*N-1-i)
#         blank = ' ' * (i//2)
#         print(blank + star)