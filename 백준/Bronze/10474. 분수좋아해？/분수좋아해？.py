while True:
    a, b = map(int, input().split())  # 테스트 케이스

    if a == 0 and b == 0:  # 종료 조건
        break

    q = a // b  # 몫
    r = a % b   # 나머지

    print(q, r, "/", b)