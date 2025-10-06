while True:
    # 세 변의 길이 입력 후 정렬
    a, b, c = sorted(map(int, input().split()))

    if a == b == c == 0:  # 종료 조건
        break

    # 피타고라스 정리 사용
    if a**2 + b**2 == c**2:
        print("right")  # 직각삼각형인 경우
    else:
        print("wrong")  # 직각삼각형이 아닌 경우