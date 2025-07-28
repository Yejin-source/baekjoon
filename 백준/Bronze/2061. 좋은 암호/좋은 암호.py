# K: 암호 후보, L: 소수 확인 범위
K, L = map(int, input().split())

# for-elae 문
for i in range(2, L):
    if K % i == 0:       # K가 i로 나누어 떨어지면
        print("BAD", i)  # i는 K를 나누는 소수 -> BAD
        break
else:
    print("GOOD")        # 나누어 떨어지지 않으면 -> GOOD