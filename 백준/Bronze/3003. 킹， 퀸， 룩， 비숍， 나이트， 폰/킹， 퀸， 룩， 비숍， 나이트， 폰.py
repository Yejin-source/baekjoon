# 체스 피스 기본 구성
standard = [1, 1, 2, 2, 2, 8]

# 현재 가지고 있는 피스의 개수
pieces = list(map(int, input().split()))


# 체스 피스는 6종류로 고정 -> 0부터 5까지 반복 
for i in range(6):
    # 기본 피스 개수 - 현재 피스 개수
    checkmate = standard[i] - pieces[i]
    print(checkmate, end=" ")