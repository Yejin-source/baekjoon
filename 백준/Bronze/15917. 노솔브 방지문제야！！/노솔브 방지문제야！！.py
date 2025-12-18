import sys

input = sys.stdin.readline

Q = int(input())  # 쿼리 개수

for _ in range(Q):

    a = int(input())  # 자연수

    # a가 2의 거듭제곱이면 1, 아니면 0
    if a > 0 and (a & (a-1)) == 0:
        print(1)
    else:
        print(0)