n = int(input())  # 점의 개수

# 각 사분면과 축의 개수 초기화
q1 = q2 = q3 = q4 = axis = 0

for _ in range(n):
    x, y = map(int, input().split())

    if x == 0 or y == 0:   # 축에 있는 경우
        axis += 1
    elif x > 0 and y > 0:  # 1사분면
        q1 += 1
    elif x < 0 and y > 0:  # 2사분면
        q2 += 1
    elif x < 0 and y < 0:  # 3사분면
        q3 += 1
    elif x > 0 and y < 0:  # 4사분면
        q4 += 1

# f-string 사용
print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")
print(f"Q4: {q4}")
print(f"AXIS: {axis}")