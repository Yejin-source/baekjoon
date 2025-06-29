# 배달 할 설탕 무게
N = int(input())

# 사용한 봉지 개수
count = 0

while N >= 0:
    # 5kg 봉지로 나누어떨어지는 경우
    if N % 5 == 0:
        count += N // 5  # 5kg 봉지 개수 추가
        print(count)
        break            # 반복 종료
    
    N -= 3      # 3kg 봉지 하나 사용
    count += 1  # 봉지 개수 추가
    
else:
    # 정확히 나눠지지 않는 경우
    print(-1)