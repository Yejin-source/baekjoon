from math import isqrt

M, N = map(int, input().split())

for i in range(M, N+1):  # M 이상 N 이하
    if i < 2:            # 0과 1 제외
        continue

    prime = True  # 일단 i가 소수라고 가정

    for j in range(2, isqrt(i) + 1):  # √i까지 검사
        if i % j == 0:     # 약수 발견 시
            prime = False  # 소수 X
            break
    if prime:
        print(i)  # 소수 출력