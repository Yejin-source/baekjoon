N = int(input())

nums = []

for i in range(N):
    num = int(input())
    nums.append(num)  

# 리스트를 오름차순으로 정렬
nums.sort()  # sort(): 원본 리스트 정렬

# 정렬된 리스트의 값을 하나씩 출력
for val in nums:
    print(val)
        
        
# 이전 코드 (수정 전)   
    
# lst = sorted(nums)  # 정렬된 새 리스트 생성

# for val in lst:
#     print(val)

# -> 코드 간소화 및 메모리 절약을 위해 sort()로 수정