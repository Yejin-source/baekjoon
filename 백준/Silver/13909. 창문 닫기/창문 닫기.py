N = int(input())  # 창문 개수 및 사람 수

# 약수 개수가 홀수인 수(=완전제곱수)만 마지막에 열려 있음
# 따라서 1부터 N까지의 완전제곱수 개수 = ⌊√N⌋
print(int(N**0.5))  # 열려 있는 창문 개수


# 다른 풀이 (isqrt)

# import math

# N = int(input())
# print(int(math.isqrt(N)))


# math.isqrt(x)
# x의 제곱근의 정수 부분(버림) 반환