N = int(input())

first = N  # 처음 값 저장
cnt = 0    # 사이클 길이

while True:
    left = N // 10  # 십의 자리
    right = N % 10  # 일의 자리
    
    # 새로운 수로 갱신
    N = right * 10 + (left + right) % 10
    
    cnt += 1
    
    # 처음 값으로 돌아오면 종료
    if N == first:  
        break

print(cnt)