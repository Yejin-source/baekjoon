a, b = map(int, input().split())

result = 1

for i in range(a, b+1):
    sum = i * (i+1) // 2  # 1부터 i까지의 합
    result = (result * sum) % 14579

print(result)