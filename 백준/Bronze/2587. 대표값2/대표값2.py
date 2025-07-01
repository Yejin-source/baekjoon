nums = []

# 5개의 정수를 입력받아 리스트에 추가
for _ in range(5):
    n = int(input())
    nums.append(n)

# 오름차순 정렬
nums.sort()

print(sum(nums)//5)  # 평균 (정수)
print(nums[2])       # 중앙값