T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    # d: 병렬 개발 시간, n: 프로그램 실행 횟수, s: 직렬 실행 시간, p: 병렬 실행 시간
    d, n, s, p = list(map(int, input().split()))
    
    if d + p*n == n*s:   # 직렬화와 병렬화를 통한 시간이 같은 경우
        print("does not matter")
    elif d + p*n > n*s:  # 병렬이 더 오래 걸리는 경우
        print("do not parallelize")
    else:                # 병렬이 더 빠른 경우
        print("parallelize")