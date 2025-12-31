while True:
    S = input()  # 숫자 카드놀이 시작값

    if S == '0':
        break

    print(S, end=' ')

    # 한 자리 수가 나오기 전까지 반복
    while len(S) > 1:
        prod = 1
        
        for ch in S:
            prod *= int(ch)

        S = str(prod)
        print(S, end=' ')

    print()