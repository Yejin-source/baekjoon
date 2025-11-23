T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    d = int(input())  # 수업시간(분)

    t = 0
    
    while t*t + t <= d:  # 최대 시간 t 계산
        t += 1

    print(t-1)  # 조건을 넘기기 전 최대 t 출력