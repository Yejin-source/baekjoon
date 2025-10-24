# 두 정수
N = int(input())
F = int(input())

N = N - (N % 100)  # N의 마지막 두 자리를 00으로 설정

for i in range(100):       # 0부터 99까지 N에 더하기
    if (N+i) % F == 0:     # F로 나누어 떨어지는지 확인
        print(f"{i:02d}")  # 두 자리로 출력
        break