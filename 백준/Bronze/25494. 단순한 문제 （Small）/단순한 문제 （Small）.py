T = int(input())  # 테스트 케이스 수

for _ in range(T):
    # 세 정수
    a, b, c = map(int, input().split())
    
    # x=y=z일 수 있는 경우의 수
    print(min(a, b, c))