# 거스름돈 액수
n = int(input())

# 초기값 (거슬러줄 수 없는 경우)
result = -1

# 5원 동전 개수를 줄여가며 확인
for five in range(n // 5, -1, -1):
    rest = n - five * 5
    
    if rest % 2 == 0:  # 2원으로 나누어 떨어지면
        result = five + rest // 2
        break

print(result)