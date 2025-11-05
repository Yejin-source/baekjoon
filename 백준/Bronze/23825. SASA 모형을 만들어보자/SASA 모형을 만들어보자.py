# N: S 블록 수, M: A 블록 수
N, M = map(int, input().split())

# 만들 수 있는 SASA 모형 최댓값 출력
print(min(N//2, M//2))