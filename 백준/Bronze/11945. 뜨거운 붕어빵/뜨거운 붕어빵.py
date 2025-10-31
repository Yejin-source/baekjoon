N, M = map(int, input().split())  # 두 정수

for _ in range(N):
    shape = input()     # 붕어빵 모양
    print(shape[::-1])  # 좌우로 뒤집어 출력