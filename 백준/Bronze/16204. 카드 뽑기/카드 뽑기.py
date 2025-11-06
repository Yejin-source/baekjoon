# N: 전체 카드 수, M: 앞면 O 개수, K: 뒷면에 적을 O 개수
N, M, K = map(int, input().split())

# 같은 모양인 카드 개수
print(min(M, K) + min(N-M, N-K))