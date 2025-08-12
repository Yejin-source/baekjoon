# 개선 코드: 중복 로직 함수화

# 트로피의 개수
N = int(input())

# 각 트로피의 높이
heights = [int(input()) for _ in range(N)]

# 한 방향에서 보이는 트로피 개수 계산
def count_visible(trophies):
    count = 0    # 보이는 개수
    highest = 0  # 현재 최고 높이
    
    for height in trophies:
        if height > highest:  # 최고 높이를 넘은 경우
            count += 1        # 트로피 개수 증가
            highest = height  # 최고 높이 갱신
    return count

print(count_visible(heights))            # 왼쪽에서 보이는 개수
print(count_visible(reversed(heights)))  # 오른쪽에서 보이는 개수


# 이전 코드: 왼쪽/오른쪽 로직 별도 구현으로 코드 중복

# 왼쪽에서 보이는 개수
# count_left = 0
# highest = 0
# for height in heights:
#     if height > highest:
#         count_left += 1
#         highest = height

# 오른쪽에서 보이는 개수
# count_right = 0
# highest = 0
# for height in reversed(heights):
#     if height > highest:
#         count_right += 1
#         highest = height