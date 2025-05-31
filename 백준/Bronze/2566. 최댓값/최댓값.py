# 최댓값 저장 변수
# 입력값 0 이상 -> 첫 비교에서 무조건 갱신되도록 -1로 초기화
max_val = -1

max_row = 0  # 최댓값 행 번호
max_col = 0  # 최댓값 열 번호


# 9개의 행 반복
for i in range(9):
    row = list(map(int, input().split()))

    # 현재 행의 각 열 반복
    for j in range(9):
        # 더 큰 값을 만나면 최댓값 갱신
        if row[j] > max_val:
            max_val = row[j]
            max_row = i + 1
            max_col = j + 1

print(max_val)
print(max_row, max_col)