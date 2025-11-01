# K: 과자 가격, N: 과자 개수, M: 가진 돈
K, N, M = map(int, input().split())  

# 필요한 총 금액
total = K * N  

# 받아야 하는 금액 계산
if total > M:
    print(total - M)  
else:
    print(0)