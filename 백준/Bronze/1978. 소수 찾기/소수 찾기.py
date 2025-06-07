# 수의 개수
N = int(input())

# N개의 수 -> 정수 리스트로 변환
nums = list(map(int, input().split()))

# 소수 개수
count = 0


# 각 숫자를 반복
for n in nums:
    if n < 2:     # 0과 1은 소수 X
        continue  # 건너뛰기

    # 2부터 n-1까지 반복
    for i in range(2, n):
        if n % i == 0:  # 나누어떨어지면 약수 존재 -> 소수 X
            break       # 반복 중단
    else:
        # for-else문
        # break 없이 반복이 끝난 경우 -> 소수
        count += 1

print(count)