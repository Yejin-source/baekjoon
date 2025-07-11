# GCD 함수 사용한 코드
import math

# 테스트 케이스의 개수
T = int(input())

for _ in range(T):
    # 두 자연수
    A, B = map(int, input().split())

    # 최소공배수(LCM) = 두 수의 곱 // 최대공약수
    lcm = A * B // math.gcd(A, B)
    print(lcm)
    

# math.gcd(x, y)
# x와 y의 최대공약수(GCD)를 반환


# 시간 초과(TLE) 발생한 코드 _ 반복문으로 공배수 직접 탐색 (비효율적)

# T = int(input())

# for _ in range(T):
#     A, B = map(int, input().split())
    
#     # 더 큰 수부터 시작해서 공배수 찾기
#     i = max(A, B)
    
#     while True:
#         if i % A == 0 and i % B == 0:
#             print(i)  # 최소공배수 출력
#             break
#         i += 1