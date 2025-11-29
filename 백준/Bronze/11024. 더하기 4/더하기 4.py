T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    N = list(map(int, input().split()))
    print(sum(N))