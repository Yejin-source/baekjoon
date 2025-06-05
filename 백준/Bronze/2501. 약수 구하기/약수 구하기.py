# N: 정수, K: K번째 약수
N, K = map(int, input().split())

factors = []  # 약수 리스트


# 1부터 N까지 반복
for i in range(1, N+1):
    if N % i == 0:         # i가 N의 약수라면
        factors.append(i)  # 리스트에 추가


# 약수 개수가 K개 이상이면 K번째 약수 출력
if len(factors) < K:
    print(0)             # K번째 약수가 존재하지 않으면 0 출력
else:
    print(factors[K-1])  # K번째 약수 출력