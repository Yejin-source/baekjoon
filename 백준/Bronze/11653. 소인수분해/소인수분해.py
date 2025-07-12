N = int(input())

# 소인수: 2부터 시작
i = 2

# N이 1이 될 때까지 반복
while N > 1:
    
    if N % i == 0:
        print(i)  # i가 N의 소인수면 출력
        N //= i   # N에서 해당 소인수 제거
    
    else:
        i += 1    # 나누어지지 않으면 다음 숫자로 갱신