# N: 여름 일 수, T: 자라는데 걸리는 일 수,
# C: 심을 수 있는 칸 수, P: 개당 가격
N, T, C, P = map(int, input().split())

count = (N-1) // T  # 수확 가능 횟수

print(count * C * P)  # 총 수익