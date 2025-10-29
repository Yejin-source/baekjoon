total = 0

for _ in range(4):
    total += int(input())  # 각 이동 시간(초)

x = total // 60  # 분 단위
y = total % 60   # 초 단위

print(x)
print(y)