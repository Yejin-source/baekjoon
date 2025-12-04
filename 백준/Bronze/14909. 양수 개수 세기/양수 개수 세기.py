nums = list(map(int, input().split()))

count = 0

for n in nums:
    if n > 0:
        count += 1

print(count)  # 양의 정수 개수