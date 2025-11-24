T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    A, B = map(int, input().split(','))  # 콤마(,) 기준으로 분리
    print(A+B)