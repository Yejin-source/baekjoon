while True:
    a, b, c, d = map(int, input().split())  # 테스트 케이스

    if a == 0 and b == 0 and c == 0 and d == 0:  # 종료 조건
        break

    min_age = c - b   # 최소 나이
    max_age = d - a   # 최대 나이

    print(min_age, max_age)