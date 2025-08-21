while True:
    num = input()

    if num == "0":  # 입력이 0이면 반복 종료
        break

    width = 0  # 호수판의 너비

    # 각 숫자의 너비 계산
    for val in num:
        if val == "0":
            width += 4
        elif val == "1":
            width += 2
        else:
            width += 3

    # 숫자 사이 간격(len-1) + 양쪽 경계 여백(2)
    width += len(num) + 1
    
    print(width)