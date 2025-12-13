K = int(input())  # 데이터 세트 개수

for idx in range(1, K+1):
    heads = int(input())  # 히드라 머리 개수
    actions = input()     # 행동 문자열

    for act in actions:
        if act == 'c':    # 머리만 자르는 경우
            heads += 1
        elif act == 'b':  # 자른 후 불로 지지는 경우
            heads -= 1

    print(f"Data Set {idx}:")
    print(heads)
    print()  # 빈 줄 출력