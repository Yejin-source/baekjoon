# 새의 수
N = int(input())

K = 1  # 한 번에 날아가는 새의 수
time = 0

while N > 0:
    if K > N:  # K가 남은 새보다 많은 경우
        K = 1
        
    N -= K     # K마리 새가 날아감
    time += 1  # 1초 경과
    K += 1     # 날아가는 새의 수 증가

print(time)