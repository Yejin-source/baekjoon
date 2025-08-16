N = int(input())
total = 0

# i: 몫이자 나머지 (1 ~ N-1)
for i in range(1, N):
    total += i * (N+1)  # 몫과 나머지가 같은 수
        
# 합 출력
print(total)