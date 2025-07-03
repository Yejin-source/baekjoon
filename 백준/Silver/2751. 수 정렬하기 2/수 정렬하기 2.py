import sys

N = int(input())  # 수의 개수

nums = []

# N개의 수를 입력받아 리스트에 추가
for _ in range(N):
    # 빠른 입력을 위해 sys.stdin.readline() 사용
    nums.append(int(sys.stdin.readline()))

# 리스트 오름차순 정렬
nums.sort()

# 정렬된 수를 한 줄씩 출력
for val in nums:
    print(val)
    
    
# 시간 초과(TLE) 발생한 코드 _ input() 사용

# for _ in range(N):
#     num = int(input())
#     nums.append(num)

# sorted_nums = sorted(nums)

# for val in sorted_nums:
#     print(val)