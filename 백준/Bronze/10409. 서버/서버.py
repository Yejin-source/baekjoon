n, T = map(int, input().split())         # 일 개수, 제한 시간
times = list(map(int, input().split()))  # 각 일의 수행 시간

total = 0  # 현재까지 사용한 시간
count = 0  # 수행한 일 개수

for t in times:
    if total + t > T:
        break
    
    total += t
    count += 1

print(count)  # T분 안에 완료될 수 있는 일 개수