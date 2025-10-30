T = int(input())  # 테스트 케이스 수

for _ in range(T):
    # V: 꼭짓점 개수, E: 모서리 개수
    V, E = map(int, input().split())
    
    print(E-V+2)  # 면의 수 출력