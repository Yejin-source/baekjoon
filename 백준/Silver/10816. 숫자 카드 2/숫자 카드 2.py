# 숫자 카드 개수
N = int(input())

# 보유한 숫자 카드 리스트
have_cards = list(map(int, input().split()))

# 확인할 숫자 개수
M = int(input())

# 확인 대상 숫자 리스트
check_cards = list(map(int, input().split()))


card_count = {}  # 숫자 카드 개수 저장용 딕셔너리

# 보유한 카드 개수 기록
for card in have_cards:
    if card in card_count:
        card_count[card] += 1  # 이미 존재하면 +1
    else:
        card_count[card] = 1   # 처음 나온 숫자는 1로 초기화
        
# 확인할 카드 개수 출력
for card in check_cards:
    if card in card_count:
        print(card_count[card], end=' ')  # 보유한 개수 출력
    else:
        print(0, end=' ')                 # 없으면 0 출력
        
        
# 딕셔너리 생성 방법        
        
# 1. defaultdict(int) 사용
# from collections import defaultdict

# card_count = defaultdict(int)  # 기본값이 0인 딕셔너리 생성

# for card in have_cards:
#     card_count[card] += 1  # 키가 없으면 자동으로 0부터 시작


# 2. Counter 사용
# from collections import Counter

# card_count = Counter(have_cards)  # 리스트를 넘기면 자동으로 개수 계산