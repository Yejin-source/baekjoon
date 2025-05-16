# 숫자의 개수
N = int(input())

# 숫자를 문자열 형태로 받기
nums = input()

# 합계 변수
total = 0


# N번 반복
for i in range(N):
    # 각 자릿수를 정수로 변환해 계산
    total += int(nums[i]) # 문자열 인덱싱 가능
    
print(total)