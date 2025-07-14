# 숫자 카드 개수
N = int(input())

# 숫자 카드 목록: 집합(set)으로 저장
cards = set(map(int, input().split()))


# 확인할 숫자 개수
M = int(input())

# 확인할 숫자 목록
check_cards = list(map(int, input().split()))


# 각 숫자가 카드에 존재하는지 확인
for card in check_cards:
    if card in cards:
        print(1, end=' ')  # 존재하면 1 출력
    else:
        print(0, end=' ')  # 존재하지 않으면 0 출력