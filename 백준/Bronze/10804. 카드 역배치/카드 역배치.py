cards = [i for i in range(1, 21)]  # 1 ~ 20 카드

for _ in range(10):    
    # 뒤집을 구간 시작 위치(a), 끝 위치(b)
    a, b = map(int, input().split())  
    
    # 지정된 구간 뒤집기
    cards[a-1:b] = reversed(cards[a-1:b]) 

print(*cards) # 언패킹 사용 (공백으로 구분해 출력)