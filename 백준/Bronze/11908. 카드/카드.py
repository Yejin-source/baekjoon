n = int(input())  # 카드 수
cards = list(map(int, input().split()))

print(sum(cards) - max(cards))  # 최대 합