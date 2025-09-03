nums = list(map(int, input().split()))

# 오름차순 정렬인 경우
if nums == sorted(nums):
    print("ascending")

# 내림차순 정렬인 경우
elif nums == sorted(nums, reverse=True):
    print("descending")

else:
    print("mixed")