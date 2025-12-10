while True:
    N = int(input())  # 한 변에 있는 정사각형 개수

    if N == 0:
        break

    total = 0

    for i in range(1, N+1):
        total += i**2  # i×i 정사각형 개수 합

    print(total)  # 총 정사각형 개수