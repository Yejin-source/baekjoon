# 7개의 자연수 입력
nums = [int(input()) for _ in range(7)]

odds = []  # 홀수 리스트

for n in nums:
    if n % 2:  # n이 홀수라면
        odds.append(n)

# odds 가 비어있지 않다면
if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)


# 리스트 컴프리헨션
# [<값> for <변수> in <리스트> if <조건>]

# 위 for문을 리스트 컴프리헨션으로도 표현 가능
# odds = [n for n in nums if n % 2]
# -> nums에서 n을 하나씩 꺼내 홀수일 때만 리스트에 추가