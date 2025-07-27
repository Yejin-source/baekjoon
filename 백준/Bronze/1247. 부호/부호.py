# 총 3개의 테스트 셋
for _ in range(3):
    N = int(input())  # 정수의 개수
    S = sum(int(input()) for _ in range(N))  # 정수들의 합

    # 합에 따라 부호 출력
    if S == 0:
        print("0")
    elif S > 0:
        print("+")
    else:
        print("-")