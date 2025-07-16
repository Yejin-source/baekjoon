# N: 전체 개수, K: 뽑을 개수
N, K = map(int, input().split())

top = 1     # 분자: N * (N-1) * ... * (N-K+1)
bottom = 1  # 분모: K!

# 이항계수 계산
for i in range(K):
    top *= (N - i)
    bottom *= (K - i)
    
print(top // bottom)


# 이항계수
# N개 중에서 K개를 순서 없이 뽑는 경우의 수
# 공식: N! / (K! * (N-K)!)


# 내장 함수 사용 시
# from math import comb

# comb(n, k): n개 중 k개를 순서 없이 뽑는 조합의 수
# print(comb(N, K))