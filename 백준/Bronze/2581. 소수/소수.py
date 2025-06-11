# M이상 N이하의 자연수 중 소수 찾기
M = int(input())
N = int(input())

# 소수 저장 리스트
primes = []

# M부터 N까지 정수 i 반복
for i in range(M, N+1):
    count = 0  # i의 약수 개수
    
    # 1부터 i까지 반복
    for j in range(1, i+1):
        if i % j == 0:    # 나누어떨어지면 약수
            count += 1    # 약수 개수 증가            
    if count == 2:        # 약수가 1과 자기 자신뿐이라면 소수
        primes.append(i)  # 소수 리스트에 추가
        
# 소수가 없을 경우
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))  # 소수들의 합
    print(min(primes))  # 소수 중 최솟값