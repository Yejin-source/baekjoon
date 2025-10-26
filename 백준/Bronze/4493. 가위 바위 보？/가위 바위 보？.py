t = int(input())  # 테스트 케이스 수

for _ in range(t):
    n = int(input())  # 가위바위보 횟수
    p1_cnt = 0
    p2_cnt = 0

    for _ in range(n):
        a, b = input().split()  # a: player 1, b: player 2

        # 가위바위보 결과
        if a == b:
            continue
        elif (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
            p1_cnt += 1
        else:
            p2_cnt += 1

    # 승자 출력
    if p1_cnt > p2_cnt:
        print("Player 1")
    elif p2_cnt > p1_cnt:
        print("Player 2")
    else:
        print("TIE")