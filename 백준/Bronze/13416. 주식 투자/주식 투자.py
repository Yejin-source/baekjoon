T = int(input())  # 테스트 데이터

for _ in range(T):
    N = int(input())  # 주식 데이터 일수
    total = 0
    
    for _ in range(N):
        # 각 회사의 주식을 구매했을 때의 손익
        A, B, C = map(int, input().split())
        
        total += max(0, A, B, C)  # 최대 이익
    print(total)