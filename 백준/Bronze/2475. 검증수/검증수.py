# 리스트로 저장
nums = list(map(int, input().split()))

total = 0  # 변수 초기화

for n in nums:
    total += n ** 2   # 제곱한 값 누적

print(total % 10)  # 검증수 출력