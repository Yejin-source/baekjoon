from math import isqrt

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    n = int(input())  # 정수
    if n <= 2:
        print(2)
        continue

    if n % 2 == 0:  # 짝수면 홀수부터 검사
        n += 1

    while True:  # 소수를 찾을 때까지 반복
        if n > 1:
            prime = True  # 일단 n이 소수라고 가정
            
            for i in range(2, isqrt(n) + 1):  #  √n까지 나누기
                if n % i == 0:
                    prime = False
                    break

            if prime:  # 소수면 출력 후 종료
                print(n)
                break
            n += 2  # 다음 홀수 검사