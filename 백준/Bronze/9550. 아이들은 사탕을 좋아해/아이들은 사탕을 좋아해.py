T = int(input())  # 테스트 케이스 수

for _ in range(T):
    # N: 상자 수, K: 아이 한 명당 사탕 수
    N, K = map(int, input().split())  
    candies = list(map(int, input().split()))

    total = 0
    
    for c in candies:
        total += c // K

    print(total)  # 생일파티에 참석할 수 있는 최대 아이 수