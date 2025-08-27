# 네 개의 양의 정수
nums = sorted(map(int, input().split()))

# 최대 직사각형 면적 = 가장 짧은 수 × 두 번째로 큰 수
print(nums[0] * nums[2])