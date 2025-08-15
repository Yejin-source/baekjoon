chess = [input() for _ in range(8)]  # 체스판 8줄
cnt = 0  # 하얀 칸 위에 있는 말 개수

for i in range(8):  # 행
    for j in range(8):  # 열
        # (i + j)가 짝수 -> 하얀 칸
        if (i + j) % 2 == 0 and chess[i][j] == 'F':
            cnt += 1

print(cnt)