# A: 햄버거 빵 개수, B: 패티 개수
A, B = map(int, input().split())

# 만들 수 있는 최대 햄버거 개수
print(min(A//2, B))