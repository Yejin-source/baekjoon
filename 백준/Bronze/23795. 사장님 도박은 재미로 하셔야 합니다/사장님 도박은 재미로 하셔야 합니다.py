total = 0

while True:
    n = int(input())  # 정수 (배팅한 돈)
    
    if n == -1:  # 종료 조건
        break
    
    total += n   # 합계 누적
    
print(total)  # 잃은 돈 총합 출력